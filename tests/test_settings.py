import test_helper


class SettingsTest(test_helper.EnvironmentBaseTest):

    def test_env(self):
        self.assertEqual('testing', self.settings.APP_ENV)

    def test_read(self):
        self.assertEqual(test_helper.ROOT_PATH, self.settings.APP_ROOT)

    def test_write_existing_setting(self):
        self.settings.DEBUG = 'i am mad'
        current_env_content = open(self.env_file_path).readlines()
        print current_env_content
        madline = [line for line in current_env_content if line == "DEBUG = i am mad\n"][0]
        self.assertIsNotNone(madline)

    def test_can_not_write_nonexisting_setting(self):
        self.settings.MAD = 'i am mad'
        current_env_content = open(self.env_file_path).readlines()
        print current_env_content
        madline = [line for line in current_env_content if line == "MAD = i am mad\n"]
        self.assertEqual(0, len(madline))
