import flask
import os
from flask_socketio import SocketIO
import flask_sqlalchemy
from dotenv import load_dotenv
from os.path import join, dirname
import models
import logging
from Bot import Bot
from sqlalchemy.pool import NullPool

user_count = 0

# Flake 8 said long lines are bad.
bot_image1 = "https://static-1.bitchute.com/live"
bot_image2 = "/channel_images/ZBaPQppGwNka/od0Qb8vms4PDWRPACmGfjWDm_medium.jpg"
bot_image = f"{bot_image1}{bot_image2}"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("Chat Program.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

app = flask.Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

database_uri = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"poolclass": NullPool}

db = flask_sqlalchemy.SQLAlchemy(app)
db.app = app


def emit_all_messages(channel):
    logger.debug(f"Emitted a message on channel {channel}")
    all_messages = []

    dbmesg = models.Messages.query.all()
    for sent_messages in dbmesg:
        msg_data = {
            "username": sent_messages.username,
            "message": sent_messages.message,
            "profile_picture": sent_messages.profilePicture
        }
        models.db.session.close()
        all_messages.append(msg_data)
    models.db.session.close()

    socketio.emit(
        channel,
        {
            "messages": all_messages
        }

    )


def emit_connected_users(channel):
    socketio.emit(channel)


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

    bot = Bot()
    result = bot.execute_command(remove_invocation)
    return result


@app.route("/")
def index():
    msgs = []
    dbmesg = models.Messages.query.all()
    for sent_messages in dbmesg:
        msgs.append(sent_messages.message)
        models.db.session.close()

    logger.debug(f"Database returned: {msgs}")
    return flask.render_template(
        "index.html"
    )
    models.db.session.close()


@socketio.on('connect')
def on_connect():
    global user_count
    logger.debug("A client connected to the server.")
    logger.debug("Emitting back all the messages to the connected user.")
    emit_all_messages("message receieved")
    socketio.emit(
        "user_connected",
        {
            "user_count": user_count,
        }
    )


@socketio.on('new message')
def new_message(data):
    logger.debug("Receieved a new_message event, flask called it.")
    message = data["message"]
    username = data["username"]
    pfp = data["profile_picture"]
    logger.debug(f"The message contained: {message}")

    db.session.add(models.Messages(username, message, pfp))
    db.session.commit()
    models.db.session.close()
    if (message.startswith("!! ")):
        botstr = message
        logger.debug("Recognized bot invocation")
        bot_return = handle_bot_invoke(botstr)
        logger.debug(f"Bot said back to command: {bot_return}")
        db.session.add(models.Messages("BOT", bot_return, bot_image))
        models.db.session.close()
        db.session.commit()
        models.db.session.close()
        logger.debug("Bots response was committed to database")

    logger.debug("Record committed to database")
    emit_all_messages("message receieved")


@socketio.on('user_logged_in')
def new_user(data):
    global user_count
    user_count += 1
    logger.debug(f"User log in Function user_count is: {user_count}")
    socketio.emit(
        "user_connected",
        {
            "user_count": user_count,
        }
    )


@socketio.on("disconnect")
def on_disconnect():
    models.db.session.close()
    global user_count
    user_count -= 1
    if (user_count < 0):
        user_count = 0
    logger.debug(f"Disconnected Function user_count is: {user_count}")
    logger.debug("A client disconnected from the server")
    socketio.emit(
        "user_disconnected",
        {
            "user_count": user_count,
        }
    )


if (__name__ == "__main__"):
    socketio.run(
        app,
        debug=True,
        port=int(os.getenv("PORT", 8080)),
        host=os.getenv("IP", "0.0.0.0")
    )
