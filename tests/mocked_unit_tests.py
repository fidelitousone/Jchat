import unittest
from unittest import mock
from freezegun import freeze_time
import sys
sys.path.append(".")
from Bot import Bot # noqa


class TestMocked(unittest.TestCase):
    translated = "| kr4V3d d4 57RenGt]-[ 4N|) d4 k3R7aIN7y ()f Zt331"
    successful_response = {
            "success": {
                "total": 1
            },
            "contents": {
                "translated": translated,
                "text": "I craved the strength and the certainty of steel",
                "translation": "leetspeak"
            }
        }

    failed_response = {
        "error": {
            "code": 404,
            "message": "Not Found"
        }
    }

    def setUp(self):
        self.bot = Bot()

    def tearDown(self):
        pass

    @freeze_time("2069-04-20")
    def test_day_command(self):
        result = self.bot.execute_command("day")
        self.assertEqual(result, "Apr-20-2069")

    @mock.patch("requests.Response.json", return_value=successful_response)
    def test_funtranslate_command(self, mock):
        invocation = "funtranslate"
        command = " I craved the strength and the certainty of steel"
        result = self.bot.execute_command(f"{invocation}{command}")
        expect = "| kr4V3d d4 57RenGt]-[ 4N|) d4 k3R7aIN7y ()f Zt331"
        self.assertEqual(result, expect)


if (__name__ == '__main__'):
    unittest.main()
