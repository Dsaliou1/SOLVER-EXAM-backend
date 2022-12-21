from .. import db,app  #qu'est-ce qu'il fait?
from ..models.epreuve import Epreuve
from ..models.schemas.schema_epreuve import SchemaEpreuve
from flask import jsonify, Blueprint, request, abort
from apifairy import authenticate, body, response

import json

epreuve = Blueprint("epreuve", __name__)
epreuve_schema = SchemaEpreuve()
epreuves_schema = SchemaEpreuve(many=True)


#ajouter un epreuve
@epreuve.route("/epreuve", methods=["POST"])
@body(epreuve_schema)
@response(epreuve_schema, 201)
def ajouter_epreuve(data):
    # data = json.loads(request.data)
    epreuve = Epreuve(**data)
    db.session.add(epreuve)
    db.session.commit()
    return epreuve


#liste des epreuve
@epreuve.route("/epreuve", methods=["GET"])
@response(epreuves_schema, 201)
def all_epreuve():
    # data = json.loads(request.data)
    return db.session.scalars(Epreuve.select()).all()


#rechercher epreuve
@epreuve.route("/epreuve/<int:id>", methods=["GET"])
@response(epreuve_schema, 200)
def get(id):
    return db.session.get(Epreuve, id) or abort(404)


# modifier epreuve
@epreuve.route("/epreuve/<int:id>", methods=["PUT"])
@body(epreuve_schema)
@response(epreuve_schema, 200)
def put(data, id):
    epreuve = db.session.get(Epreuve, id) or abort(404)
    epreuve.update(data)
    db.session.commit()
    return epreuve


#suppression d'un epreuve
@epreuve.route("/epreuve/<int:id>", methods=["DELETE"])
@response(epreuve_schema, 200)
def delete(id):
    epreuve = db.session.get(Epreuve, id) or abort(404)
    db.session.delete(epreuve)
    db.session.commit()
    return epreuve
db.create_all()