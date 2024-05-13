from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.register import register_user
from models.login import login_user

# Create an instance of Blueprint for authentication
auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Retrieve the form data
        username = request.form.get("username")
        password = request.form.get("password")

        # Call the login function
        if login_user(username, password):
            # Authentication successful, redirect to success page
            flash("Login successful", "success")
            return redirect(url_for("main.home"))  # Replace "success" with the name of your success route
        else:
            # Authentication failed, display error message
            flash("Invalid username or password", "error")

    # Render the login template
    return render_template("login.html")


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get form data
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        surname = request.form.get("surname")

        # Call the register_user function to handle registration
        success = register_user(username, email, password, name, surname)

        if success:
            # Registration successful, redirect to login page
            return redirect(url_for("auth.login"))
        else:
            # Registration failed, render register page with error message
            return render_template("register.html", error="Registration failed. Please try again.")

    # If request method is GET, render the register page
    return render_template("register.html")

@auth_blueprint.route("/success")
def success():
    return "Login successful! You are now redirected to the success page."