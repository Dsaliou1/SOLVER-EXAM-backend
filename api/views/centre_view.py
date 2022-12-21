from .. import db,app  #qu'est-ce qu'il fait?
from ..models.centre import Centre
from ..models.schemas.schema_centre import SchemaCentre
from flask import jsonify, Blueprint, request, abort
from apifairy import authenticate, body, response

import json

centre = Blueprint("centre", __name__)
centre_schema = SchemaCentre()
centres_schema = SchemaCentre(many=True)


#ajouter un centre
@centre.route("/centre", methods=["POST"])
@body(centre_schema)
@response(centre_schema, 201)
def ajouter_centre(data):
    # data = json.loads(request.data)
    centre = Centre(**data)
    db.session.add(centre)
    db.session.commit()
    return centre


#liste des centre
@centre.route("/centre", methods=["GET"])
@response(centres_schema, 201)
def all_centre():
    # data = json.loads(request.data)
    return db.session.scalars(Centre.select()).all()


#rechercher centre
@centre.route("/centre/<int:id>", methods=["GET"])
@response(centre_schema, 200)
def get(id):
    return db.session.get(Centre, id) or abort(404)


# modifier centre
@centre.route("/centre/<int:id>", methods=["PUT"])
@body(centre_schema)
@response(centre_schema, 200)
def put(data, id):
    centre = db.session.get(Centre, id) or abort(404)
    centre.update(data)
    db.session.commit()
    return centre


#suppression d'un centre
@centre.route("/centre/<int:id>", methods=["DELETE"])
@response(centre_schema, 200)
def delete(id):
    centre = db.session.get(Centre, id) or abort(404)
    db.session.delete(centre)
    db.session.commit()
    return centre
db.create_all()