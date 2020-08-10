import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = 'PubScore'
app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/overview")
def overview():
    sorted_score = mongo.db.competitors.find().sort('score', -1)
    return render_template("overview.html",
                           competitors=sorted_score)


@app.route("/updateteams")
def updateteams():
    sorted_teamname = mongo.db.competitors.find().sort('team_name', 1)
    return render_template("updateteams.html",
                           competitors=sorted_teamname)


@app.route('/updatescore/<competitor_id>/<competitor_name>/<score>',
           methods=['POST'])
def updatescore(competitor_id, competitor_name, score):
    competitors = mongo.db.competitors
    points_scored = int(request.form.get('points_scored'))
    old_score = int(score)
    new_score = old_score + points_scored
    now = datetime.datetime.now()
    today = now.strftime("%d-%m-%Y")
    competitors.update({'_id': ObjectId(competitor_id)},
                       {
                           'team_name': competitor_name,
                           'score': new_score,
                           'last_update': today
                       })
    return redirect(url_for('updateteams'))


@app.route('/deleteteam/<competitor_id>')
def deleteteam(competitor_id):
    mongo.db.competitors.remove({'_id': ObjectId(competitor_id)})
    return redirect(url_for('updateteams'))


@app.route("/addteam")
def addteam():
    return render_template("addteam.html")


@app.route('/insertteam', methods=['POST'])
def insertteam():
    competitors = mongo.db.competitors
    name = (request.form.get("team_name"))
    points = int(request.form.get("score"))
    competitors.insert(
        {
            "team_name": name,
            "score": points
        })
    return redirect(url_for('overview'))


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
