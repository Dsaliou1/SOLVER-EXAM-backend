from .. import db,app
from ..models.utilisateurs import Utilisateur
from flask import jsonify
@app.route("/utilisateurs",methods=["POST"])
def ajouter_utilisateur(data):
    utilisateur = Utilisateur(**data)
    db.session.add(utilisateur)
    db.session.commit()
    return jsonify(
        nom=utilisateur.nom,
        prenom=utilisateur.prenom
    )