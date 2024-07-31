#!/usr/bin/python3
""" a bash script that starts a flask web application."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function that prints hello hbnb at the root"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function that displays hello hbnb at the root."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ displays 'C' followed by the value of d var
    ( replace underscore _ symbol with a space)
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
