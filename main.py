import flask 
import os
from flask_socketio import SocketIO
import flask_sqlalchemy
from dotenv import load_dotenv
from os.path import join, dirname

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
db.init_app(app)
db.app = app

db.create_all()
db.session.commit()

@app.route("/")
def index():
    return flask.render_template(
        "index.html"
    )

@socketio.on('connect')
def on_connect():
    print("User connected to the server.")
    socketio.emit('connected', {
        'test': 'Connected'
    })

@socketio.on('new message')
def new_message(data):
    message = data["message"]
    print("Received a message from user.")
    print(f"Message sent was: {message}")
    socketio.emit(
        "message receieved",
        {
            "message": message
        }
    )


if (__name__=="__main__"):
    socketio.run(
        app,
        debug=True,
        port=int(os.getenv("PORT", 8080)),
        host=os.getenv("IP", "127.0.0.1")
    )