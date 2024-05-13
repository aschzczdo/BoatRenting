from flask import Blueprint, render_template
from flask_login import login_required

gallery_blueprint = Blueprint("gallery", __name__)


@gallery_blueprint.route("/gallery")
def get_gallery():
    return render_template("gallery.html")
