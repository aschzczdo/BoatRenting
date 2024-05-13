from flask import Blueprint, render_template


# Create an instance of Blueprint for 404
error_blueprint = Blueprint("error", __name__)


@error_blueprint.route("/404")
def maintenance():
    return render_template("404.html")
