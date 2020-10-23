import unittest
from unittest import mock
from freezegun import freeze_time
import json
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

    tmr = " hour exceeded."
    too_many_req = f"Too Many Requests: Rate limit of 5 requests per{tmr}"
    too_many_req2 = " Please wait for 15 minutes and 00 seconds."
    err_str = f"{too_many_req}{too_many_req2}"
    overuse_response = {
        "error": {
            "code": 429,
            "message": f"{err_str}"
        }
    }

    failed_message = json.dumps(failed_response)

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

    @mock.patch("requests.Response.json", return_value=failed_response)
    def test_funtranslate_command_fail(self, mock):
        invocation = "funtranslate"
        command = " I craved the strength and the certainty of steel"
        result = self.bot.execute_command(f"{invocation}{command}")
        self.assertEqual(result, "Not Found")

    @mock.patch("requests.Response.json", return_value=overuse_response)
    def test_funtranslate_overuse(self, mock):
        invocation = "funtranslate"
        command = " I craved the strength and the certainty of steel"
        result = self.bot.execute_command(f"{invocation}{command}")
        self.assertEqual(result, self.err_str)


if (__name__ == '__main__'):
    unittest.main()
