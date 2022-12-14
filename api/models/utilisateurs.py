from .. import db
import sqlalchemy as sqla
class Utilisateur(db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    nom = sqla.Column(sqla.String(100), nullable=True)
    prenom = sqla.Column(sqla.String(200), nullable=True)