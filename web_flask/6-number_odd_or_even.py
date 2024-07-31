#!/usr/bin/python3
""" a bash script that starts a flask web application."""
from flask import Flask, render_template

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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_routte(text):
    """ Dispay “Python ”, followed by the value of d var
    (replace underscore _ symbols with a space )
    """
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ Displays 'n is a number' only if n is an int."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if n is an integer
    H1 tag: "Number: n" inside d Body tag
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_0dd_or_even(n):
    """Displays an HTML page only if n is an int.
    H1 tag: 'Number: n is even|odd' inside d body tag.
    """
    dev = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', number=n dev=dev)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
