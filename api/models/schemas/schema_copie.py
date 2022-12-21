from ... import ma
from ..models import Copie


class SchemaCopie(ma.SQLAlchemySchema):
    class Meta:
        model = Copie
        ordered = True

    id_copie = ma.auto_field(dump_only=True)
    note = ma.Float(required=True)
    matiere = ma.String(required=False)


