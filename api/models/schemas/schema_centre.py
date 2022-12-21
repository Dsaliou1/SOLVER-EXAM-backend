from ... import ma
from ..models import Centre


class SchemaCentre(ma.SQLAlchemySchema):
    class Meta:
        model = Centre
        ordered = True

    id_centre = ma.String(required=True)
    session = ma.String(required=True)  # annee
    nom_centre = ma.String(required=True)
    ia = ma.String(required=True)
    ief = ma.String(required=True)
    numero_jury = ma.String(required=True)
