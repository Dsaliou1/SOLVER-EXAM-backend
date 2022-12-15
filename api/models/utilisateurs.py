from api import db
import sqlalchemy as sqla
class Updateable:
    def update(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)
class Utilisateur(Updateable,db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    nom = sqla.Column(sqla.String(100), nullable=True)
    prenom = sqla.Column(sqla.String(200), nullable=True)