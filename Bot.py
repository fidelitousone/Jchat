from datetime import date
import requests


class Bot:
    URL = "https://api.funtranslations.com/translate/leetspeak.json"
    UNKNOWN_COMMAND = "Unknown command, type !! help for a list of commands."

    def execute_command(self, command):
        try:
            command_itself = command.split(" ")[0]
        except AttributeError:
            return self.UNKNOWN_COMMAND

        if command_itself == "about":
            return "Just a simple chat bot, type !! help for some commands."
        elif command_itself == "help":
            return "Commands: !! about, !! help, !! funtranslate, !! day"
        elif command_itself == "funtranslate":
            fun_translate_args = command.split("funtranslate")[1]
            payload = {"text": f"{fun_translate_args}"}
            r = requests.get(self.URL, params=payload)
            resp = r.json()
            try:
                translated_text = resp["contents"]["translated"]
                return translated_text
            except KeyError:
                return resp["error"]["message"]

        elif command_itself == "day":
            today = date.today()
            day = today.strftime("%b-%d-%Y")
            return day
        else:
            return self.UNKNOWN_COMMAND
