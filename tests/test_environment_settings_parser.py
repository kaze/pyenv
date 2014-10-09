import os
import unittest

import test_helper
from config.environment import EnvironmentSettingsParser


class EnvironmentSettingsParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = EnvironmentSettingsParser()

    def test_remove_quotes(self):
        original = " hello world ' while  ' it is True        "
        result = "hello world ' while  ' it is True"

        self.assertEqual(result, self.parser.remove_quotes(original))

    def test_try_parsing_boolean(self):
        originals = ["YES", "no", "false", "True", "ON", "off"]
        result = [True, False, False, True, True, False]

        self.assertEqual(result, [self.parser.try_parsing_boolean(item) for item in originals])

    def test_parse_simple(self):
        original = "$HOME"
        result = os.environ['HOME']

        self.assertEqual(result, self.parser.parse_simple(original))

    def test_parse_list(self):
        original = "( '2', '$HOME  ', yes, 'FALSE  ')"
        result = ['2', os.environ['HOME'], True, False]

        self.assertEqual(result, self.parser.parse_list(original))

    def test_parse(self):
        original_list = "( ' 2', ' $HOME  ', yes, 'FALSE  ')"
        result_list = ['2', os.environ['HOME'], True, False]

        self.assertEqual(result_list, self.parser.parse_list(original_list))

    def test_get_value_pair(self):
        line = "'TEST_VARS' = \" ( '2', '$HOME  ', yes, 'FALSE  ')  \""
        result = ("TEST_VARS", "( '2', '{}  ', yes, 'FALSE  ')".format(os.environ['HOME']))

        self.assertEqual(result, self.parser.get_value_pair(line))

