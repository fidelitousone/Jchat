import unittest
import sys
sys.path.append(".")
from Bot import Bot # noqa
from main import handle_bot_invoke # noqa


class TestUnmocked(unittest.TestCase):

    def setUp(self):
        self.bot = Bot()

    def tearDown(self):
        pass

    def test_about_command(self):
        result = self.bot.execute_command("about")
        expect = "Just a simple chat bot, type !! help for some commands."
        self.assertEqual(result, expect)

    def test_help_command(self):
        result = self.bot.execute_command("help")
        expect = "Commands: !! about, !! help, !! funtranslate, !! day"
        self.assertEqual(result, expect)

    def test_unknown_command(self):
        garbage_data = "nlsdackas dllasd"
        result = self.bot.execute_command(garbage_data)
        self.assertEqual(result, self.bot.UNKNOWN_COMMAND)

    def test_funtranslate_url(self):
        API_LINK = "https://api.funtranslations.com"
        LEETSPEAK_URL = f"{API_LINK}/translate/leetspeak.json"
        self.assertEqual(LEETSPEAK_URL, self.bot.URL)

    def test_handle_bot_invoke(self):
        result = handle_bot_invoke("!! about")
        expect = "Just a simple chat bot, type !! help for some commands."
        self.assertEqual(result, expect)


if (__name__ == '__main__'):
    unittest.main()
