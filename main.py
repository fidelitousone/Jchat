from os.path import join, dirname
import os
import flask
from flask_socketio import SocketIO
import flask_sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.pool import NullPool
from Bot import Bot
# pylint: disable=no-member
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-envvar-default
# pylint: disable=global-statement
# pylint: disable=no-absolute-import

user_count = 0


BOT_IMAGE = """
https://static-1.bitchute.com/live/channel_images/
ZBaPQppGwNka/od0Qb8vms4PDWRPACmGfjWDm_medium.jpg
"""


app = flask.Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)

database_uri = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"poolclass": NullPool}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = flask_sqlalchemy.SQLAlchemy(app)
db.app = app
import models  # noqa # pylint: disable=wrong-import-position


def emit_all_messages(channel):
    all_messages = []

    dbmesg = models.Messages.query.all()
    for sent_messages in dbmesg:
        msg_data = {
            "username": sent_messages.username,
            "message": sent_messages.message,
            "profile_picture": sent_messages.profilePicture,
        }
        models.db.session.close()
        all_messages.append(msg_data)
    models.db.session.close()

    socketio.emit(channel, {"messages": all_messages})


def emit_connected_users(channel):
    socketio.emit(channel)


def handle_bot_invoke(string):
    try:
        remove_invocation = string.split("!! ")[1]
    except AttributeError:
        return "Invalid invoke, bot did not execute!"

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

    return flask.render_template("index.html")


@socketio.on("connect")
def on_connect():
    global user_count
    emit_all_messages("message receieved")
    socketio.emit(
        "user_connected",
        {
            "user_count": user_count,
        },
    )


@socketio.on("new message")
def new_message(data):

    message = data["message"]
    username = data["username"]
    pfp = data["profile_picture"]

    db.session.add(models.Messages(username, message, pfp))
    db.session.commit()
    models.db.session.close()
    if message.startswith("!! "):
        botstr = message

        bot_return = handle_bot_invoke(botstr)

        db.session.add(models.Messages("BOT", bot_return, BOT_IMAGE))
        models.db.session.close()
        db.session.commit()
        models.db.session.close()

    emit_all_messages("message receieved")


@socketio.on("user_logged_in")
def new_user(data):
    global user_count
    user_count += 1

    socketio.emit(
        "user_connected",
        {
            "user_count": user_count,
        },
    )


@socketio.on("disconnect")
def on_disconnect():
    global user_count
    user_count -= 1
    if user_count < 0:
        user_count = 0
    socketio.emit(
        "user_disconnected",
        {
            "user_count": user_count,
        },
    )


if __name__ == "__main__":
    socketio.run(
        app,
        debug=True,
        port=int(os.getenv("PORT", 8080)),
        host=os.getenv("IP", "0.0.0.0"),
    )
