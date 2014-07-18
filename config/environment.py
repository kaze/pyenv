import importlib
import os
import sys


class EnvironmentSettingsParser(object):
    def remove_quotes(self, value):
        return str(value.strip().strip("'").strip('"').strip())

    def try_parsing_boolean(self, value):
        if value.lower() in ['true', 'yes', 'on']:
            return True
        elif value.lower() in ['false', 'no', 'off']:
            return False

        return value

    def parse_simple(self, value):
        value = os.path.expandvars(value)
        value = self.try_parsing_boolean(value)

        return value

    def parse_list(self, value):
        values = value.strip('[').strip(']').split(',')

        return [self.parse(item.strip()) for item in values]

    def parse(self, value):
        value = self.remove_quotes(str(value))

        if value.find('[') > -1 and value.find(']') > -1:
            return self.parse_list(value)

        return self.parse_simple(value)

    def get_value_pair(self, line):
        setting = line.rstrip('\n').split('=')
        key = str(self.remove_quotes(setting[0]))
        value = str(os.path.expandvars(self.remove_quotes(setting[1])))

        return key, value

    def parse_file(self, filepath):
        with open(filepath) as envfile:
            for line in envfile.readlines():
                if not line.strip() or line.startswith('#'):
                    continue
                key, value = self.get_value_pair(line)
                os.environ[key] = value


class Environment(object):
    def __init__(self, settings_file='.env', app_name=None):
        app_name = app_name or os.path.basename(os.getcwd())

        self.parser = EnvironmentSettingsParser()
        self.env_file = self.fetch('ENVIRONMENT_SETTINGS_FILE', settings_file)
        self.app_name = self.fetch('APP_NAME', app_name)

    def fetch(self, key, default=None):
        value = os.getenv(key, default)

        return self.parser.parse(value) if value else default

    def set(self, key, value):
        os.environ[key] = value

    def get_current_environment(self):
        for item in sys.argv:
            if item.find('test') > -1:
                return 'testing'

        return self.fetch('APP_ENV', 'development')

    def set_current_environment(self, filepath):
        current_env = self.get_current_environment()
        self.set('APP_ENV', current_env)

    def set_environment(self, filepath=None):
        filepath = filepath or self.env_file

        try:
            self.parser.parse_file(filepath)
            self.set_current_environment(filepath)

        except IOError:
            self.set_current_environment(filepath)

    def get_app_settings(self):
        env = self.get_current_environment()

        app_settings = "config.environments.{}".format(env)
        settings_file = importlib.import_module(app_settings)

        return settings_file.Settings()

    def get_settings(self):
        self.set_environment()

        return self.get_app_settings()

