# All the imports needed for this project
import os
from flask import (Flask, g, render_template, redirect,
                   request, url_for, session, flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime

# Import my env.py that's ignored by git
if os.path.exists("env.py"):
    import env


# Log in configuration
# Used tutorial: https://www.youtube.com/watch?v=2Zz97NVbH0U
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


SECRET_PASSWORD_ONE = os.environ.get("SECRET_PASSWORD_ONE")
SECRET_PASSWORD_TWO = os.environ.get("SECRET_PASSWORD_TWO")
users = []
users.append(User(id=1, username='Frances', password=SECRET_PASSWORD_ONE))
users.append(User(id=2, username='Admin', password=SECRET_PASSWORD_TWO))


# App instance
app = Flask(__name__)
app.secret_key = 'verysecret'

# MongoDB configuration
MONGO_URI = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = 'PubScore'
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)


# Index to welcome the user
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# Set g.user at login to show the right navigation links
# Used tutorial: https://www.youtube.com/watch?v=2Zz97NVbH0U
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


# Login for admin
# Checks if user and password are correct
# If correct, redirects to dashboard
# If incorrect, redirects to login and shows message for user
# Used tutorial: https://www.youtube.com/watch?v=2Zz97NVbH0U
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        try:
            user = [x for x in users if x.username == username][0]
        except IndexError:
            flash('Please use correct username and password')
            return redirect(url_for('login'))
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))

        flash('Please use correct username and password')
        return redirect(url_for('login'))

    return render_template("login.html")


# Dashboard after login for some explanation
@app.route("/dashboard")
def dashboard():
    if not g.user:
        return redirect(url_for('login'))

    return render_template("dashboard.html")


# Overview of all the teams in the competition
# sorted from highest to lowest score
# Everybody can view this page
@app.route("/overview")
def overview():
    sorted_score = mongo.db.competitors.find().sort('score', -1)
    return render_template("overview.html",
                           competitors=sorted_score)


# Overview of all the teams in the competiton
# From here the admin can add points for all the teams
# From here the admin can delete teams from the competition
# Sorted by teamname for easy updating
@app.route("/updateteams")
def updateteams():
    if not g.user:
        return redirect(url_for('login'))

    sorted_teamname = mongo.db.competitors.find().sort('team_name', 1)
    return render_template("updateteams.html",
                           competitors=sorted_teamname)


# Adds the scored points to the original score
# Adds or updates date of last adjustment by admin
# After update you stay on the updateteams page to do more updates
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


# Deletes team
# After update you stay on the updateteams page to do more updates
@app.route('/deleteteam/<comp_id>')
def deleteteam(comp_id):
    mongo.db.competitors.remove({'_id': ObjectId(comp_id)})
    return redirect(url_for('updateteams'))


# Add a team by using a form
@app.route("/addteam")
def addteam():
    if not g.user:
        return redirect(url_for('login'))

    return render_template("addteam.html")


# Insert team to the database
# If there is no team photo no-photo.png gets asigned
@app.route('/insertteam', methods=['POST'])
def insertteam():
    competitors = mongo.db.competitors
    name = request.form.get("team_name").capitalize()
    points = int(request.form.get("score"))
    if request.form.get("photo") == "":
        photo = "../static/images/no-photo.png"
    else:
        photo = request.form.get("photo")
    competitors.insert(
        {
            "team_name": name,
            "score": points,
            "photo": photo
        })
    return redirect(url_for('overview'))


# Contact page in case of any problems
@app.route("/contact")
def contact():
    if not g.user:
        return redirect(url_for('login'))

    return render_template("contact.html")


# Log out
# Used example from: https://www.roytuts.com/python-login-and-logout-example/
@app.route("/logout")
def logout():
    if not g.user:
        return redirect(url_for('login'))

    session.pop('user_id', None)
    return redirect(url_for('index'))


# To run the app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
