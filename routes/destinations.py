from flask import Blueprint, render_template

destinations_blueprint = Blueprint("destinations", __name__)


@destinations_blueprint.route("/destinations")
def get_all_destinations():
    return render_template("destinations.html")
