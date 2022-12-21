from ... import ma
from ..models import MembreSecretariat


class SchemaMembreSecretariat(ma.SQLAlchemySchema):
    class Meta:
        model = MembreSecretariat
        ordered = True

    id_membre_secretariat = ma.Integer(dump_only=True)
    prenom = ma.String(required=True)
    nom = ma.String(required=True)
    telephone = ma.String(required=True)
    profil = ma.String(required=True)


