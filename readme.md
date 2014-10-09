## installation

I made a pip-installable package from `pyenv`, but not published it, because it isn't mature enough. If you are in explorer mood, you can install it with:

    pip install git+https://github.com/kaze/pyenv.git

After this you can create a file named `.env` in your project's root directory, and get settings with:

    from config import settings
    print settings.HOME         #=> '/home/your-username'

## how does it work?

`pyenv` uses an environment setting file (as default, this file named `.env`, and placed into your app's root directory) to load configuration values to the application's environment, and to use those freshly loaded values to figure out which set of settings it should give you to wire up the application.

Example `.env` file:

    APP_ENV = development
    APP_NAME = nqmon

    SOME_VERY_SECRET_VARIABLE = secret

In the loading phase `pyenv` expands environment variables (they should be in the form of `$VARIABLE` or `${VARIABLE}` if you want this to happen).

    APP_ROOT = $HOME/projects/awesome_app         #=> /home/your_username/projects/awesome_app

Additionally, you can use flat arrays in the environment settings file:

    PATHS = ($HOME/projects/other, /usr/local/lib)
    ADMINS = ('me@example.com', 'you@example.com')

And booleans, too:

    DEBUG = true

Boolens could be "yes", "on", "true" for `True`, and "no", "off", "false" for `False`, case-insensitively.

## usage

You should put the `config` directory in the root of your project, and create an `.env` file with your variables. You can add this code to your app_name's `__init__.py`:

     from app_name.config.environment import Environment

     env = Environment(app_name='app_name')
     settings = env.get_settings()

Then every `UPPERCASE_WITH_UNDERSCORES` variable you wrote into the `.env` file will be accessible inside the code in this way:

    from app_name import settings
    settings.UPPERCASE_WITH_UNDERSCORES

Actually, every environment variable will be accessible in this way. If you try to read a setting which does not exists, `pyenv` tries to read the value from the similarly named environment variable. It that does not exists, too, you just get a `None`.

You can add new, environment specific settings to the corresponding `config/environments/environment_name.py` file, if you want that settings would be accessible on other machines, because you should not commit your `.env` file into the repository.

Which of those python files will be loaded on settings-initialization? This depends on the value of the APP_ENV variable, which defaulted to 'development'. You can create new environments, too, if you create a new settings file for that environment in the `config/environments` directory, named after the new environment.
