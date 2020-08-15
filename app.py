import os
from flask import Flask, render_template, g, redirect, request, url_for
from flask_oidc import OpenIDConnect
from okta import UsersClient
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
SECRET_KEY = os.environ.get("SECRET_KEY")
app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = SECRET_KEY
app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"
oidc = OpenIDConnect(app)
okta_client = UsersClient("https://dev-395248.okta.com",
                          "00SvA-wtwtZrunBeOfMPCmIdo788BQcjWq_81b3dwK")
MONGO_URI = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = 'PubScore'
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)


@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for(".dashboard"))


@app.route("/dashboard")
@oidc.require_login
def dashboard():
    return render_template("dashboard.html")


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


@app.route('/updatescore/<comp_id>/<score>',
           methods=['POST'])
def updatescore(comp_id, score):
    competitors = mongo.db.competitors
    points_scored = int(request.form.get('points_scored'))
    old_score = int(score)
    new_score = old_score + points_scored
    now = datetime.datetime.now()
    today = now.strftime("%d-%m-%Y")
    competitors.update({'_id': ObjectId(comp_id)},
                       {
                           '$set': {'score': new_score, 'last_update': today}
                       })
    return redirect(url_for('updateteams'))


@app.route('/deleteteam/<comp_id>')
def deleteteam(comp_id):
    mongo.db.competitors.remove({'_id': ObjectId(comp_id)})
    return redirect(url_for('updateteams'))


@app.route("/addteam")
def addteam():
    return render_template("addteam.html")


@app.route('/insertteam', methods=['POST'])
def insertteam():
    competitors = mongo.db.competitors
    name = (request.form.get("team_name"))
    points = int(request.form.get("score"))
    if request.form.get("photo") == "":
        photo = "placeholder_photo"
    else:
        photo = (request.form.get("photo"))
    competitors.insert(
        {
            "team_name": name,
            "score": points,
            "photo": photo
        })
    return redirect(url_for('overview'))


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
