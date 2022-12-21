from ... import ma
from ..models import Candidat


class SchemaCandidat(ma.SQLAlchemySchema):
    class Meta:
        model = Candidat
        ordered = True

    id_candidat = ma.auto_field(dump_only=True)
    numero_table = ma.Integer(required=True)
    prenom = ma.String(required=True)
    nom = ma.String(required=True)
    lieu_naissance = ma.String(required=True)
    etablissement = ma.String(required=True)
    statut = ma.String(required=True)
    date_naissance = ma.String(required=True)  #
    aptitude = ma.String(required=True)  # apt ou inapte
    sexe = ma.String(required=True)
    total_point = ma.Float(required=True) # a revoir
    etat = ma.String(required=True)  # a revoir present ou absent


