from flask import Flask, render_template
from routes.auth import auth_blueprint
from dotenv import load_dotenv
from models.db import mysql_connection
from routes.e404 import error_blueprint
from routes.gallery import gallery_blueprint
from routes.destinations import destinations_blueprint
from routes.main import main_blueprint
from routes.contact import contact_blueprint

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.register_blueprint(auth_blueprint)
app.register_blueprint(error_blueprint)
app.register_blueprint(gallery_blueprint)
app.register_blueprint(destinations_blueprint)
app.register_blueprint(contact_blueprint)


@app.route("/")
def home():
    return render_template("index.html")


app.register_blueprint(main_blueprint)


@app.route("/charters")
def charters():
    return render_template("charters.html")


if __name__ == "__main__":
    app.run(debug=True)
