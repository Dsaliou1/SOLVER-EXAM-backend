from .. import db,app  #qu'est-ce qu'il fait?
from ..models.models import Candidat
from ..models.schemas.shcema_candidat import SchemaCandidat
from flask import jsonify, Blueprint, request, abort
from apifairy import authenticate, body, response

import json

candidat = Blueprint("candidat", __name__)
candidat_schema = SchemaCandidat()
candidats_schema = SchemaCandidat(many=True)


#ajouter un candidat
@candidat.route("/candidat", methods=["POST"])
@body(candidat_schema)
@response(candidat_schema, 201)
def ajouter_candidat(data):
    # data = json.loads(request.data)
    candidat = Candidat(**data)
    db.session.add(candidat)
    db.session.commit()
    return candidat


#liste des candidat
@candidat.route("/candidat", methods=["GET"])
@response(candidats_schema, 201)
def all_candidat():
    # data = json.loads(request.data)
    return db.session.scalars(Candidat.select()).all()


#rechercher candidat
@candidat.route("/candidat/<int:id>", methods=["GET"])
@response(candidat_schema, 200)
def get(id):
    return db.session.get(Candidat, id) or abort(404)


# modifier candidat
@candidat.route("/candidat/<int:id>", methods=["PUT"])
@body(candidat_schema)
@response(candidat_schema, 200)
def put(data, id):
    candidat = db.session.get(Candidat, id) or abort(404)
    candidat.update(data)
    db.session.commit()
    return candidat


#suppression d'un candidat
@candidat.route("/candidat/<int:id>", methods=["DELETE"])
@response(candidat_schema, 200)
def delete(id):
    candidat = db.session.get(Candidat, id) or abort(404)
    db.session.delete(candidat)
    db.session.commit()
    return candidat
db.create_all()