from flask import Flask
from alchemical.flask import Alchemical
from flask_migrate import Migrate

from .models.utilisateurs import Utilisateur
from flask import jsonify

app = Flask(__name__)
app.config.from_object("config.DevConfig")
db = Alchemical(app)
migrate = Migrate(app, db)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/utilisateurs",methods=["POST"])
def ajouter_utilisateur(data):
    utilisateur = Utilisateur(**data)
    db.session.add(utilisateur)
    db.session.commit()
    return jsonify(
        nom=utilisateur.nom,
        prenom=utilisateur.prenom
    )