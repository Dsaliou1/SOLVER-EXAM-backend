from ... import ma
from ..models import Utilisateur


class SchemaUtilisateur(ma.SQLAlchemySchema):
    class Meta:
        model = Utilisateur
        ordered = True

    id = ma.auto_field(dump_only=True)
    nom = ma.String(required=True)
    prenom = ma.String(required=False)
    login = ma.String(required=False)
    mot_de_passe = ma.String(required=False)
    telephone = ma.String(required=False)
    profil = ma.String(required=False)
    email = ma.String(required=False)


