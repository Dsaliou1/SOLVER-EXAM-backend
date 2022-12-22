from ... import ma
from ..models import MembreSecretariat


class SchemaMembreSecretariat(ma.SQLAlchemySchema):
    class Meta:
        model = MembreSecretariat
        ordered = True

    id_membre_secretariat = ma.Integer(dump_only=True)

