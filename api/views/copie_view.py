from .. import db,app  #qu'est-ce qu'il fait?
from ..models.copie import Copie
from ..models.schemas.schema_copie import SchemaCopie
from flask import jsonify, Blueprint, request, abort
from apifairy import authenticate, body, response

import json

copie = Blueprint("copie", __name__)
copie_schema = SchemaCopie()
copies_schema = SchemaCopie(many=True)


#ajouter un copie
@copie.route("/copie", methods=["POST"])
@body(copie_schema)
@response(copie_schema, 201)
def ajouter_copie(data):
    # data = json.loads(request.data)
    copie = Copie(**data)
    db.session.add(copie)
    db.session.commit()
    return copie


#liste des copie
@copie.route("/copie", methods=["GET"])
@response(copies_schema, 201)
def all_copie():
    # data = json.loads(request.data)
    return db.session.scalars(Copie.select()).all()


#rechercher copie
@copie.route("/copie/<int:id>", methods=["GET"])
@response(copie_schema, 200)
def get(id):
    return db.session.get(Copie, id) or abort(404)


# modifier copie
@copie.route("/copie/<int:id>", methods=["PUT"])
@body(copie_schema)
@response(copie_schema, 200)
def put(data, id):
    copie = db.session.get(Copie, id) or abort(404)
    copie.update(data)
    db.session.commit()
    return copie


#suppression d'un copie
@copie.route("/copie/<int:id>", methods=["DELETE"])
@response(copie_schema, 200)
def delete(id):
    copie = db.session.get(Copie, id) or abort(404)
    db.session.delete(copie)
    db.session.commit()
    return copie
db.create_all()