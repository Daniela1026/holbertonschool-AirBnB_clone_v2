#!/usr/bin/python3
"line of text variable"
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    "this is a line of text"
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    "this is a line of text"
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def lan(text):
    "this is a line of text"
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
