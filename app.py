import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/overview")
def overview():
    return render_template("overview.html")


@app.route("/updatescore")
def updatescore():
    return render_template("updatescore.html")


@app.route("/addteam")
def addteam():
    return render_template("addteam.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
