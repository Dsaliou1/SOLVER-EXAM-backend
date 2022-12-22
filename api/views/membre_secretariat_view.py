from .. import db,app  #qu'est-ce qu'il fait?
from ..models.models import MembreSecretariat
from ..models.schemas.schema_membre_secretariat import SchemaMembreSecretariat
from flask import jsonify, Blueprint, request, abort
from apifairy import authenticate, body, response

import json

membre_secretariat = Blueprint("membre_secretariat", __name__)
membre_secretariat_schema = SchemaMembreSecretariat()
membre_secretariats_schema = SchemaMembreSecretariat(many=True)


#ajouter un membre_secretariat
@membre_secretariat.route("/membre_secretariat", methods=["POST"])
@body(membre_secretariat_schema)
@response(membre_secretariat_schema, 201)
def ajouter_membre_secretariat(data):
    # data = json.loads(request.data)
    membre_secretariat = MembreSecretariat(**data)
    db.session.add(membre_secretariat)
    db.session.commit()
    return membre_secretariat


#liste des membre_secretariat
@membre_secretariat.route("/membre_secretariat", methods=["GET"])
@response(membre_secretariats_schema, 201)
def all_membre_secretariat():
    # data = json.loads(request.data)
    return db.session.scalars(MembreSecretariat.select()).all()


#rechercher membre_secretariat
@membre_secretariat.route("/membre_secretariat/<int:id>", methods=["GET"])
@response(membre_secretariat_schema, 200)
def get(id):
    return db.session.get(MembreSecretariat, id) or abort(404)


# modifier membre_secretariat
@membre_secretariat.route("/membre_secretariat/<int:id>", methods=["PUT"])
@body(membre_secretariat_schema)
@response(membre_secretariat_schema, 200)
def put(data, id):
    membre_secretariat = db.session.get(MembreSecretariat, id) or abort(404)
    membre_secretariat.update(data)
    db.session.commit()
    return membre_secretariat


#suppression d'un membre_secretariat
@membre_secretariat.route("/membre_secretariat/<int:id>", methods=["DELETE"])
@response(membre_secretariat_schema, 200)
def delete(id):
    membre_secretariat = db.session.get(MembreSecretariat, id) or abort(404)
    db.session.delete(membre_secretariat)
    db.session.commit()
    return membre_secretariat
db.create_all()