from ... import ma
from ..models import Epreuve


class SchemaEpreuve(ma.SQLAlchemySchema):
    class Meta:
        model = Epreuve
        ordered = True

    id_epreuve = ma.Integer(dump_only=True)
    libelle = ma.String(required=True)
    coefficient = ma.Integer(required=True)
    type_epreuve = ma.String(required=True)  # 1er tour ou 2nd tour



