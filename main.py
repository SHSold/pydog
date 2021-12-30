# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_function():
    return "<h1>Hello Stefan</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
