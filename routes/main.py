from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.register import register_user
from models.login import login_user


# Create an instance of Blueprint for authentication
main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/")
def home():
    return render_template("index.html")