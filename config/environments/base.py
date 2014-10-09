class BaseSettings(object):
    def __init__(self, environment):
        self.env = environment

        # current environment's name
        self.ENV = self.env.get_environment_name()

        # debugging
        self.DEBUG = self.env.fetch('DEBUG', False)

    def __getattr__(self, name):
        if name in self.__dict__:
            return object.__getattr__(self, name)
        else:
            return self.env.fetch(name)

    def __setattr__(self, name, value):
        if name in self.__dict__:
            return self.env.write(name, value)
        else:
            return object.__setattr__(self, name, value)
