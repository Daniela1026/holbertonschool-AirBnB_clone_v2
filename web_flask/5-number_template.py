#!/usr/bin/python3
"""
Display a HTML page only if n is an integer
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Displays "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Displays "C" followed by the text in <text>.
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """
    Displays "Python" followed by the text in <text>.
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def vernumber(n):
    return '{} is a number'.format(escape(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def funct(n):
    """ Display a HTML page only if n is an integer """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
