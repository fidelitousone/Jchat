import flask 
import os
from flask_socketio import SocketIO
import flask_sqlalchemy
from dotenv import load_dotenv
from os.path import join, dirname
import models
import logging
import requests
from datetime import date

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter  = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("Chat Program.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

app = flask.Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

sql_user = os.environ["SQL_USER"]
sql_password = os.environ["SQL_PASSWORD"]
database_uri = f"postgresql://{sql_user}:{sql_password}@localhost/postgres"



app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.app = app




def emit_all_messages(channel):
    logger.debug(f"Emitted a message on channel {channel}")
    all_messages = []
        
    dbmesg = models.Messages.query.all()
    for sent_messages in dbmesg:
        all_messages.append(f"{sent_messages.username}: {sent_messages.message}")

    socketio.emit(channel,
        {
            "messages": all_messages
        }
    
    )

def handle_bot_invoke(string):
    remove_invocation = string.split("!! ")[1]
    logger.debug(remove_invocation)
    command = remove_invocation.split(" ")[0]
    try:
        commandarg = remove_invocation.split(" ")[1]
    except IndexError:
        commandarg = "no args"
    logger.debug(f"Bot handler got command: {command}")
    logger.debug(f"Command Arguments are: {commandarg}")
    if (command == "about"):
        return "Just a simple chat bot, type !! help for some commands."
    elif (command == "help"):
        return  "Commands: !! about, !! help, !! funtranslate, !! day"
    elif (command == "funtranslate"):
        fun_translate_args = remove_invocation.split("funtranslate")[1]
        logger.debug("text args are: " + fun_translate_args)
        url = "https://api.funtranslations.com/translate/leetspeak.json"
        payload = {
            "text": f"{fun_translate_args}"
        }
        r = requests.get(url, params=payload)
        logger.debug("Calling URL: " + r.url)
        resp = r.json()
        logger.debug(f"funtranslate API returned this json: {resp}")
        translated_text = resp["contents"]["translated"]
        logger.debug(f"Got message back: {translated_text}")
        return translated_text
    elif (command == "day"):
        today = date.today()
        day = today.strftime("%b-%d-%Y")
        return day
    else:
        return "Unknown command, type !! help for a list of commands."

@app.route("/")
def index():
    models.db.create_all()
    msgs = []
    dbmesg = models.Messages.query.all()
    for sent_messages in dbmesg:
        msgs.append(sent_messages.message)
        
    logger.debug(f"Database returned: {msgs}")
    return flask.render_template(
        "index.html"
    )

@socketio.on('connect')
def on_connect():
    logger.debug("A client connected to the server.")
    logger.debug("Emitting back all the messages to the connected user.")
    emit_all_messages("message receieved")
    

@socketio.on('new message')
def new_message(data):
    logger.debug("Receieved a new_message event, flask called it.")
    message = data["message"]
    logger.debug(f"The message contained: {message}")
    

    
    db.session.add(models.Messages("User", message))
    db.session.commit()
    if (message.startswith("!! ")):
        botstr = message
        logger.debug("Recognized bot invocation")
        bot_return = handle_bot_invoke(botstr)
        logger.debug(f"Bot said back to command: {bot_return}")
        db.session.add(models.Messages("BOT", bot_return))
        db.session.commit()
        logger.debug("Bots response was committed to database")
    
    logger.debug(f"Record committed to database")
    emit_all_messages("message receieved")
    
@socketio.on("disconnect")
def on_disconnect():
    logger.debug("A client disconnected from the server")


if (__name__=="__main__"):
    socketio.run(
        app,
        debug=True,
        port=int(os.getenv("PORT", 8080)),
        host=os.getenv("IP", "127.0.0.1")
    )