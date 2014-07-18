class BaseSettings(object):
    def __init__(self, environment):
        self.env = environment

        # current environment's name
        self.ENV = self.env.get_environment_name()

        # debugging
        self.DEBUG = self.env.fetch('DEBUG', False)

    def __getattr__(self, name):
        if not name in self.__dict__:
            return self.env.fetch(name)
        else:
            return object.__getattr__(self, name)
