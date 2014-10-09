import os
import sys
import unittest

import test_helper
from config.environment import Environment


env_content = '''APP_ENV = "staging"
APP_ROOT = $PWD

# stress test
'TEST_VARS' = " ( '2', '$HOME  ', yes, 'FALSE  ')  "
'''


class EnvironmentTest(unittest.TestCase):
    def setUp(self):
        env_file_path = 'tests/fixtures/.env'
        self.env = Environment(env_file=env_file_path)
        with open(env_file_path, 'w') as envfile:
            envfile.write(env_content)
        self.env.set_environment()

    def tearDown(self):
        os.environ['APP_ENV'] = ''
        os.environ['APP_ROOT'] = ''
        os.environ['NONEXISTENT_SETTING'] = ''
        os.environ['EXISTENT_SETTING'] = ''
        os.environ['TEST_VARS'] = ''

    def test_fetch(self):
        self.assertEqual(os.environ['HOME'], self.env.fetch('HOME'))
        self.assertEqual(None, self.env.fetch('NONEXISTENT_SETTING'))
        self.assertEqual('default', self.env.fetch('NONEXISTENT_SETTING', 'default'))

    def test_set(self):
        self.env.set('EXISTENT_SETTING', 'something')
        self.assertEqual('something', os.environ['EXISTENT_SETTING'])

    def test_test_environment(self):
        self.assertEqual('testing', os.environ['APP_ENV'])

    def test_set_environment(self):
        self.env.set_environment('tests/fixtures/.env')
        self.assertEqual(os.environ['PWD'], os.environ['APP_ROOT'])
        self.assertEqual(['2', '/Users/kaze', True, False], self.env.fetch('TEST_VARS'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(EnvironmentTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
