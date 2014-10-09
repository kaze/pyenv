from os.path import abspath, join, basename
import sys

ROOT_PATH = abspath(join(basename(__file__), '..'))

if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)


import os
import unittest

from config.environment import Environment


env_content = '''APP_ENV = "staging"
APP_ROOT = $PWD

# stress test
'TEST_VARS' = " ( '2', '$HOME  ', yes, 'FALSE  ')  "
'''


class EnvironmentBaseTest(unittest.TestCase):

    def setUp(self):
        self.env_file_path = 'tests/fixtures/.env'
        self.env = Environment(env_file=self.env_file_path)
        with open(self.env_file_path, 'w') as envfile:
            envfile.write(env_content)
        self.env.set_environment()
        self.settings = self.env.get_app_settings()

    def tearDown(self):
        os.environ['APP_ENV'] = ''
        os.environ['APP_ROOT'] = ''
        os.environ['NONEXISTENT_SETTING'] = ''
        os.environ['EXISTENT_SETTING'] = ''
        os.environ['TEST_VARS'] = ''
