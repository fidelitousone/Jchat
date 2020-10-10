import flask 
import os
from flask_socketio import SocketIO

app = flask.Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

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


if (__name__=="__main__"):
    socketio.run(
        app,
        debug=True,
        port=int(os.getenv("PORT", 8080)),
        host=os.getenv("IP", "127.0.0.1")
    )