from distutils.core import setup


setup(name='pyenv',
      version='0.1.0',
      url='https://github.com/kaze/pyenv',
      download_url='git+ssh://git@github.com:kaze/pyenv.git',
      maintainer='Zsolt Kormany',
      maintainer_email='zsoltkormany@gmail.com',
      py_modules=[
        'config.environment',
        'config.environments.base',
        'config.environments.development',
        'config.environments.production',
        'config.environments.staging',
        'config.environments.testing'
      ])
