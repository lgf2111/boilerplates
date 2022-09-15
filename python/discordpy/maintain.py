from flask import Flask
from waitress import serve
from threading import Thread

app = Flask(__name__)


@app.route("/")
def home():
    return ""


def run():
    serve(app, host="0.0.0.0", port=8000)


def maintain():
    t = Thread(target=run)
    t.start()
