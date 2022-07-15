from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Configuración Flask Login
login_manager = LoginManager()
login_manager.init_app(app)

# Configuración SQLAlchemy
app.config["SECRET_KEY"] = "deeceba3e9acee8672e253a419ca2ca300e83918" # Generado con secrets.token_hex()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:password@server/db".format("admin","administrador","localhost","loginflask")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)