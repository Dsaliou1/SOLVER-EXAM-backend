from ... import ma
from ..models import Correcteur


class SchemaCorrecteur(ma.SQLAlchemySchema):
    class Meta:
        model = Correcteur
        ordered = True

    id_correcteur = ma.auto_field(dump_only=True)


