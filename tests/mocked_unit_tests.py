import unittest
from unittest import mock
from freezegun import freeze_time
import json
import sys
sys.path.append(".")
from Bot import Bot # noqa
from main import emit_connected_users, new_message, new_user, on_connect
from main import index, on_disconnect


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

    front_end_resp = {
        "message": "look at the TOP of his head",
        "username": "ben_dover@gmail.com",
        "profile_picture": "www.example.com"
    }

    front_end_resp_bot = {
        "message": "!! help",
        "username": "ben_dover@gmail.com",
        "profile_picture": "www.example.com"
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

    @mock.patch("flask_socketio.SocketIO.emit")
    def test_emit_connected_users(self, mock):
        emit_connected_users("pickle asmr")
        mock.assert_called_with("pickle asmr")

    @mock.patch("flask_socketio.SocketIO.emit")
    @mock.patch("main.emit_all_messages")
    def test_on_connect(self, mock, mock1):
        on_connect()

    @mock.patch("flask_socketio.SocketIO.emit")
    def test_new_user(self, mock):
        data = "who put on this planet eugh"
        new_user(data)

    @mock.patch("flask_socketio.SocketIO.emit")
    def test_on_disconnect(self, mock):
        on_disconnect()

    @mock.patch("models.db.session")
    def test_on_new_message(self, mock):
        new_message(self.front_end_resp)

    @mock.patch("models.db.session")
    def test_new_msg_bot(self, mock):
        new_message(self.front_end_resp_bot)

    @mock.patch("models.db.session")
    @mock.patch("flask.render_template")
    def test_index(self, mock, mock1):
        index()


if (__name__ == '__main__'):
    unittest.main()
