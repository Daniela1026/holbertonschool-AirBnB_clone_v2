#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_lis', strict_slashes=False)
def states_list():
    """ State list """
    states = storage.all("State")
    states = [state for state in states.values()]
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Method to handle """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)