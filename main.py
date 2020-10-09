import flask 
import os

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template(
        "index.html"
    )

if (__name__=="__main__"):
    app.run(
        debug=True,
        port=int(os.getenv("PORT", 8080)),
        host=os.getenv("IP", "localhost")
    )