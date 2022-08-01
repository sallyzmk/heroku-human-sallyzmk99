# -*- coding:utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(port=5000)