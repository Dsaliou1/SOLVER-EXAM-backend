from .. import db,app  #qu'est-ce qu'il fait?
from ..models.correcteur import Correcteur
from ..models.schemas.schema_correcteur import SchemaCorrecteur
from flask import jsonify, Blueprint, request, abort
from apifairy import authenticate, body, response

import json

correcteur = Blueprint("correcteur", __name__)
correcteur_schema = SchemaCorrecteur()
correcteurs_schema = SchemaCorrecteur(many=True)


#ajouter un correcteur
@correcteur.route("/correcteur", methods=["POST"])
@body(correcteur_schema)
@response(correcteur_schema, 201)
def ajouter_correcteur(data):
    # data = json.loads(request.data)
    correcteur = Correcteur(**data)
    db.session.add(correcteur)
    db.session.commit()
    return correcteur


#liste des correcteur
@correcteur.route("/correcteur", methods=["GET"])
@response(correcteurs_schema, 201)
def all_correcteur():
    # data = json.loads(request.data)
    return db.session.scalars(Correcteur.select()).all()


#rechercher correcteur
@correcteur.route("/correcteur/<int:id>", methods=["GET"])
@response(correcteur_schema, 200)
def get(id):
    return db.session.get(Correcteur, id) or abort(404)


# modifier correcteur
@correcteur.route("/correcteur/<int:id>", methods=["PUT"])
@body(correcteur_schema)
@response(correcteur_schema, 200)
def put(data, id):
    correcteur = db.session.get(Correcteur, id) or abort(404)
    correcteur.update(data)
    db.session.commit()
    return correcteur


#suppression d'un correcteur
@correcteur.route("/correcteur/<int:id>", methods=["DELETE"])
@response(correcteur_schema, 200)
def delete(id):
    correcteur = db.session.get(Correcteur, id) or abort(404)
    db.session.delete(correcteur)
    db.session.commit()
    return correcteur
db.create_all()