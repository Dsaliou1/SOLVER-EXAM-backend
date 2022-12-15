from .. import db,app
from ..models.utilisateurs import Utilisateur
from ..models.schema_utilisateur import SchemaUtilisateur
from flask import jsonify, Blueprint, request
from apifairy import authenticate, body, response

import json

utilisateurs = Blueprint("utilisateurs", __name__)
utilisateur_schema=SchemaUtilisateur()
utilisateurs_schema=SchemaUtilisateur(many=True)

@utilisateurs.route("/utilisateurs",methods=["POST"])
@body(utilisateur_schema)
@response(utilisateur_schema, 201)
def ajouter_utilisateur(data):
    # data = json.loads(request.data)
    utilisateur = Utilisateur(**data)
    db.session.add(utilisateur)
    db.session.commit()
    return utilisateur
@utilisateurs.route("/utilisateurs",methods=["GET"])
@response(utilisateurs_schema, 201)
def all_utilisateur():
    # data = json.loads(request.data)
    return db.session.scalars(Utilisateur.select()).all()

db.create_all()