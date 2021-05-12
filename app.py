"""
Code adapted from the Task Manager Flask app
from the CI course material.
"""

import os
import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Render Home template


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# User authentication and management

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "is_admin": "off",
            "date_joined": datetime.datetime.utcnow()
        }
        mongo.db.users.insert_one(sign_up)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Signed Up Successfully!")
        return redirect(url_for("account", username=session["user"]))
    return render_template("sign_up.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "account", username=session["user"]))
            else:
                # invalid password match
                flash("Username and/or password is incorrect")
                return redirect(url_for("sign_in"))

        else:
            # username doesn't exist
            flash("Username and/or password is incorrect")
            return redirect(url_for("sign_in"))

    return render_template('sign_in.html')


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # get the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("account.html", username=username)

    return redirect(url_for("sign_in"))


@app.route("/sign_out")
def sign_out():
    # remove user from session cookies
    session.clear()
    flash("You have been signed out")
    return redirect(url_for("sign_in"))


# Games CRUD functionality

@app.route("/get_games")
def get_games():
    games = list(mongo.db.games.find())
    return render_template(
        "get_games.html",
        games=games)


@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        shop_link = (
            "https://store.steampowered.com/search/?term=" +
            request.form.get("name"))
        game = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "image_url": request.form.get("image_url"),
            "number_players": request.form.get("number_players"),
            "year_release": request.form.get("year_release"),
            "genre": request.form.get("genre"),
            "developer": request.form.get("developer"),
            "publisher": request.form.get("publisher"),
            "platforms": request.form.get("platforms"),
            "shop_link": shop_link,
            "created_by": session["user"],
            "created_date": datetime.datetime.utcnow(),
        }
        mongo.db.games.insert_one(game)
        flash("Game Successfully Submitted")
        return redirect(url_for("get_games"))
    genres = mongo.db.genres.find().sort("genre", 1)
    return render_template("add_game.html", genres=genres)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    games = list(mongo.db.games.find(
        {"$text": {"$search": query}}))
    return render_template(
        "get_games.html", games=games)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
