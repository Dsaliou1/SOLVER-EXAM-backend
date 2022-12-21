from ... import ma
from ..models import Correcteur


class SchemaCorrecteur(ma.SQLAlchemySchema):
    class Meta:
        model = Correcteur
        ordered = True

    id_correcteur = ma.auto_field(dump_only=True)
    matricule = ma.String(required=True)
    prenom = ma.String(required=False)
    nom = ma.String(required=False)
    specialite = ma.String(required=False)
    telephone = ma.String(required=False)


