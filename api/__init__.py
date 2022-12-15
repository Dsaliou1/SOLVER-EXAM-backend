from flask import Flask, redirect, url_for
from alchemical.flask import Alchemical
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from apifairy import APIFairy
app = Flask(__name__)
app.config.from_object("config.DevConfig")
db = Alchemical(app)
migrate = Migrate(app, db)
ma=Marshmallow()
ma.init_app(app)
apifairy=APIFairy()
apifairy.init_app(app)

from .views.utilisateurs_view import utilisateurs
app.register_blueprint(utilisateurs, url_prefix="/api")

@app.route("/")
def index():  # pragma: no cover
    return redirect(url_for("apifairy.docs"))

