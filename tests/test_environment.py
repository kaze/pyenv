import os
import sys
import unittest

import test_helper


env_content = '''APP_ENV = "staging"
APP_ROOT = $PWD

# stress test
'TEST_VARS' = " ( '2', '$HOME  ', yes, 'FALSE  ')  "
'''


class EnvironmentTest(test_helper.EnvironmentBaseTest):

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
