from flask import Blueprint, render_template

dashboard_blueprint = Blueprint("dashboard", __name__)


@dashboard_blueprint.route("/dashboard")
def dashboard():
    # Dummy data for demonstration
    dummy_data = {
        "username": "John Doe",
        "email": "john.doe@example.com",
        "role": "Admin",
    }
    
    return render_template("dashboard.html", data=dummy_data)
