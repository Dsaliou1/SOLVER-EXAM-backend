from ... import ma
from ..utilisateurs import Utilisateur


class SchemaUtilisateur(ma.SQLAlchemySchema):
    class Meta:
        model = Utilisateur
        ordered = True

    id = ma.auto_field(dump_only=True)
    nom = ma.String(required=True)
    prenom = ma.String(required=False)


