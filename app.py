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


# render home template
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
            flash("Username already exists", "negative-feedback")
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
        flash("Signed Up Successfully!", "positive-feedback")
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
                    request.form.get("username")), "positive-feedback")
                return redirect(url_for(
                    "account", username=session["user"]))
            else:
                # invalid password match
                flash(
                    "Username and/or password is incorrect",
                    "negative-feedback")
                return redirect(url_for("sign_in"))

        else:
            # username doesn't exist
            flash("Username and/or password is incorrect", "negative-feedback")
            return redirect(url_for("sign_in"))

    return render_template('sign_in.html')


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # defensive programming to prevent brute force
    if session.get("user"):
        # get the session user's username from the db
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        user_favourites = list(mongo.db.favourites.find(
            {"user_id": ObjectId(user["_id"])}))
        user_comments = list(mongo.db.comments.find(
            {"user_id": user}))
        if session["user"]:
            return render_template(
                "account.html", username=username,
                user=user, user_favourites=user_favourites,
                user_comments=user_comments)

        return redirect(url_for("sign_in"))
    flash("You need to be signed in to see your account!", "negative-feedback")
    return redirect(url_for("sign_in"))


@app.route("/sign_out")
def sign_out():
    # remove user from session cookies
    session.clear()
    flash("You have been signed out", "positive-feedback")
    return redirect(url_for("sign_in"))


# Games CRUD functionality

# display all games on get_games template
@app.route("/get_games")
def get_games():
    games = list(mongo.db.games.find())
    return render_template(
        "get_games.html",
        games=games)


# find game and show its related comments
@app.route("/game/<game_id>", methods=["GET", "POST"])
def game(game_id):
    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    comments = list(mongo.db.comments.find({"game_id": ObjectId(game_id)}))
    return render_template("game.html", game=game, comments=comments)


# add new game to the db
@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    # defensive programming to prevent brute force
    if session.get("user"):
        if request.method == "POST":
            # create shopping link based on the game name
            shop_link = (
                "https://store.steampowered.com/search/?term=" +
                request.form.get("name"))
            # gather game info from the form
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
            # write new game info in the db
            mongo.db.games.insert_one(game)
            flash("Game Successfully Submitted", "positive-feedback")
            return redirect(url_for("get_games"))
        genres = mongo.db.genres.find().sort("genre", 1)
        return render_template("add_game.html", genres=genres)
    flash("You need to be signed in to add a game!", "negative-feedback")
    return redirect(url_for("sign_in"))


# edit a game from the db
@app.route("/edit_game/<game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    # defensive programming to prevent brute force
    if session.get("user"):
        if request.method == "POST":
            username = mongo.db.users.find_one(
                {"username": session["user"]})
            game = mongo.db.games.find_one(
                {"_id": ObjectId(game_id)})
            # allows edit only if created by user in session or admin
            if (session["user"] == game["created_by"] or
                    username["is_admin"] == "on"):
                # create shopping link based on the game name
                shop_link = (
                    "https://store.steampowered.com/search/?term=" +
                    request.form.get("name"))
                # gather game info from the form
                update_game = {
                    "name": request.form.get("name"),
                    "description": request.form.get("description"),
                    "image_url": request.form.get("image_url"),
                    "number_players": request.form.get("number_players"),
                    "year_release": request.form.get("year_release"),
                    "genre": request.form.get("genre"),
                    "developer": request.form.get("developer"),
                    "publisher": request.form.get("publisher"),
                    "platforms": request.form.get("platforms"),
                    "shop_link": shop_link
                }
                # update job info in the db
                mongo.db.games.update_one(
                    {"_id": ObjectId(game_id)},
                    {"$set": update_game})
                flash("Game Successfully Updated", "positive-feedback")
        game = mongo.db.games.find_one({"_id": ObjectId(game_id)})
        genres = mongo.db.genres.find().sort("genre", 1)
        return render_template("edit_game.html", game=game, genres=genres)
    flash("You need to be signed in to edit a game!", "negative-feedback")
    return redirect(url_for("sign_in"))


# delete a game from the db
@app.route("/delete_game/<game_id>")
def delete_game(game_id):
    # defensive programming to prevent brute force
    if session.get("user"):
        username = mongo.db.users.find_one(
                {"username": session["user"]})
        game = mongo.db.games.find_one(
                {"_id": ObjectId(game_id)})
        # allows delete only if created by user in session or admin
        if (session["user"] == game["created_by"] or
                username["is_admin"] == "on"):
            mongo.db.games.delete_one({"_id": ObjectId(game_id)})
            flash("Game Successfully Deleted", "positive-feedback")
            return redirect(url_for("get_games"))
    flash("You need to be signed in to delete a game!", "negative-feedback")
    return redirect(url_for("sign_in"))


# search a game in the db by text query
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    games = list(mongo.db.games.find(
        {"$text": {"$search": query}}))
    return render_template(
        "get_games.html", games=games)


# allows registered users to post a comment
@app.route("/add_comment/<game_id>", methods=["POST", "GET"])
def add_comment(game_id):
    # defensive programming to prevent brute force
    if session.get("user"):
        if request.method == "POST":
            # find username
            username = mongo.db.users.find_one(
                {"username": session["user"]})
            # find game
            game = mongo.db.games.find_one(
                {"_id": ObjectId(game_id)})
            # gather comment info to write in the db
            comment = {
                "game_id": game["_id"],
                "game_name": game["name"],
                "user_id": username,
                "date_submitted": datetime.datetime.utcnow(),
                "text": request.form.get("comment")
            }
            # write comment to the db
            mongo.db.comments.insert_one(comment)
            flash("Comment Successfully Posted!", "positive-feedback")
            return redirect(url_for("game", game_id=game_id))
    flash("You need to be signed in to leave a comment!", "negative-feedback")
    return redirect(url_for("sign_in"))


# allows registered users to add a game as favourite
@app.route("/add_favourite/<game_id>")
def add_favourite(game_id):
    # defensive programming to prevent brute force
    if session.get("user"):
        # find user
        user = mongo.db.users.find_one(
                {"username": session["user"]})
        # find game
        game = mongo.db.games.find_one(
                {"_id": ObjectId(game_id)})
        # gather favourite info to write in the db
        favourite = {
            "game_id": game["_id"],
            "user_id": user["_id"],
            "game_name": game["name"],
            "game_image": game["image_url"]
        }
        # check if the game is already marked as favourite
        cursor = mongo.db.favourites.find_one(
            {"game_id": game["_id"],
                "user_id": user["_id"]})
        if cursor is not None:
            flash("You've already added this game!", "negative-feedback")
        else:
            # if game is not favourited, then it writes the info to the db
            mongo.db.favourites.insert_one(favourite)
            flash("Added to account's favourites!", "positive-feedback")
        return redirect(url_for("game", game_id=game_id))
    flash(
        "You need to be signed in to add this game as favourite!",
        "negative-feedback")
    return redirect(url_for("sign_in"))


# route to display terms and conditions template
@app.route("/terms_and_conditions")
def terms_and_conditions():
    return render_template("terms_and_conditions.html")


# route to display privacy policy template
@app.route("/privacy_policy")
def privacy_policy():
    return render_template("privacy_policy.html")


# error handler for errors type 404
@app.errorhandler(404)
def not_found(error):
    # displays an error page and redirects the user
    not_found_image = url_for('static', filename='images/404-error.jpg')
    return render_template(
        "error-handlers/404.html", error=error,
        not_found_image=not_found_image)


# error handler for errors type 503
@app.errorhandler(503)
def service_unavailable(error):
    # displays an error page and redirects the user
    service_unavailable_image = url_for(
        'static', filename='images/503-error.jpg')
    return render_template(
        "error-handlers/503.html", error=error,
        service_unavailable_image=service_unavailable_image)


# error handler for errors type 500
@app.errorhandler(500)
def internal_server(error):
    # displays an error page and redirects the user
    internal_server_image = url_for(
        'static', filename='images/500-error.jpg')
    return render_template(
        "error-handlers/500.html", error=error,
        internal_server_image=internal_server_image)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
