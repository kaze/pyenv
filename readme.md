## how does it work?

`pyenv` uses an environment setting file (as default, this file named `.env`, and placed in your app's root directory) to load configuration values to the application's environment, and to use those freshly loaded values to figure out which set of settings it should give you to wire up the application.

Example `.env` file:

    APP_ENV = development
    APP_NAME = nqmon

    SOME_VERY_SECRET_VARIABLE = secret

In the loading phase `pyenv` expands environment variables (which should be in the form of `$VARIABLE` or `${VARIABLE}`) to their values.

    APP_ROOT = $HOME/projects/awesome_app         #=> /home/your_username/projects/awesome_app

Additionally, you can use flat arrays in the environment settings file:

    PATHS = [$HOME/projects/other, /usr/local/lib]
    ADMINS = ['me@example.com', 'you@example.com']

## usage

You should put the `config` directory in the root of your project, and create an `.env` file with your variables. `pyenv` will try to figure out the current environment from the value of the `APP_ENV` variable.

Flask example:

    from flask import Flask
    from config.environment import Environment

    def create_app():
        env = Environment()
        settings = env.get_settings()
        app_name = env.fetch('APP_NAME')

        app = Flask(app_name)

        return app
