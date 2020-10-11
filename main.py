import flask 
import os
from flask_socketio import SocketIO
import flask_sqlalchemy
from dotenv import load_dotenv
from os.path import join, dirname
import models
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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
    all_messages = [ \
        db_message.message for db_message \
        in db.session.query(models.Messages).all()]
    
    socketio.emit(channel,
        {
            "messages": all_messages
        }
    
    )

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
    db.session.add(models.Messages("User",message))
    db.session.commit()
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