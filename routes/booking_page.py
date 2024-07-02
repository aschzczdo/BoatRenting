from flask import Blueprint, render_template

booking_blueprint = Blueprint("booking", __name__)


@booking_blueprint.route("/booking")
def contact():
    return render_template("booking_page.html")
