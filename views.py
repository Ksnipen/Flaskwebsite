from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "/")

@views.route("/")
def home():
    return render_template("index.html", randnumb = get_random_number())

@views.route("/profile")
def profile():
    return render_template("profile.html")

@views.route("/json")
def get_json():
    return jsonify({'name': 'Kenneth', 'coolness': 10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/home")
def go_to_home():
    return redirect(url_for("views.home"))