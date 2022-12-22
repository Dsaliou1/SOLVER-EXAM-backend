from .. import db,app  #qu'est-ce qu'il fait?
from ..models.models import Utilisateur
from ..models.schemas.schema_utilisateur import SchemaUtilisateur
from flask import jsonify, Blueprint, request, abort
from apifairy import authenticate, body, response

import json

utilisateur = Blueprint("utilisateur", __name__)
utilisateur_schema=SchemaUtilisateur()
utilisateurs_schema=SchemaUtilisateur(many=True)


#ajouter un utilisateur
@utilisateur.route("/utilisateur",methods=["POST"])
@body(utilisateur_schema)
@response(utilisateur_schema, 201)
def ajouter_utilisateur(data):
    # data = json.loads(request.data)
    utilisateur = Utilisateur(**data)
    db.session.add(utilisateur)
    db.session.commit()
    return utilisateur


#liste des utilisateurs
@utilisateur.route("/utilisateur",methods=["GET"])
@response(utilisateurs_schema, 201)
def all_utilisateur():
    # data = json.loads(request.data)
    return db.session.scalars(Utilisateur.select()).all()


#rechercher utilisateur
@utilisateur.route("/utilisateur/<int:id>", methods=["GET"])
@response(utilisateur_schema, 200)
def get(id):
    return db.session.get(Utilisateur, id) or abort(404)


# modifier utilisateur
@utilisateur.route("/utilisateur/<int:id>", methods=["PUT"])
@body(utilisateur_schema)
@response(utilisateur_schema, 200)
def put(data, id):
    utilisateur = db.session.get(Utilisateur, id) or abort(404)
    utilisateur.update(data)
    db.session.commit()
    return utilisateur


#suppression d'un utilisateur
@utilisateur.route("/utilisateur/<int:id>", methods=["DELETE"])
@response(utilisateur_schema, 200)
def delete(id):
    utilisateur = db.session.get(Utilisateur, id) or abort(404)
    db.session.delete(utilisateur)
    db.session.commit()
    return utilisateur
db.create_all()