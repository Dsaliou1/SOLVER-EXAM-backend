from api import db
import sqlalchemy as sqla


class Updateable:
    def update(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)


affectation_correcteur = db.Table('affectation_correcteur',
                                  db.Column('correcteur_id', db.Integer, db.ForeignKey('correcteur.id'),
                                            primary_key=True),
                                  db.Column('centre_id', db.Integer, db.ForeignKey('centre.id'), primary_key=True),
                                  db.Column('session', db.Integer, primary_key=False)
                                  )

evaluation = db.Table('evaluation',
                      db.Column('candidat_id', db.Integer, db.ForeignKey('candidat.id'), primary_key=True),
                      db.Column('epreuve_id', db.Integer, db.ForeignKey('epreuve.id'), primary_key=True)
                      )


affectation_candidat = db.Table('affectation_candidat',
                                db.Column('candidat_id', db.Integer, db.ForeignKey('candidat.id'), primary_key=True),
                                db.Column('centre_id', db.Integer, db.ForeignKey('centre.id'), primary_key=True),
                                db.Column('session', db.Integer, primary_key=False)
                                )


affectation_membre_secretariat = db.Table('affectation_membre_secretariat',
                                          db.Column('membre_secretariat_id', db.Integer,
                                                    db.ForeignKey('membre_secretariat.id'), primary_key=True),
                                          db.Column('centre_id', db.Integer, db.ForeignKey('centre.id'), primary_key=True),
                                          db.Column('session', db.Integer, primary_key=False)
                                          )


class Utilisateur(Updateable, db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    nom = sqla.Column(sqla.String(200), nullable=True)
    prenom = sqla.Column(sqla.String(200), nullable=True)
    login = sqla.Column(sqla.String(200), nullable=True)
    mot_de_passe = sqla.Column(sqla.String(200), nullable=True)
    telephone = sqla.Column(sqla.String(200), nullable=True)
    profil = sqla.Column(sqla.String(200), nullable=True)
    email = sqla.Column(sqla.String(200), nullable=True)
    correcteur_id = db.relationship('Correcteur', backref='utilisateur', uselist=False)
    membre_secretariat_id = db.relationship('MembreSecretariat', backref='utilisateur', uselist=False)
    candidat_id = db.relationship('Candidat', backref='utilisateur', uselist=False)


class Candidat(Updateable, db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    numero_table = sqla.column(sqla.Integer, nullable=False)
    lieu_naissance = sqla.Column(sqla.String(200), nullable=False)
    etablissement = sqla.Column(sqla.String(200), nullable=False)
    date_naissance = sqla.Column(sqla.String(200), nullable=False)  #
    aptitude = sqla.Column(sqla.String(200), nullable=False)  # apt ou inapte
    sexe = sqla.Column(sqla.String(200), nullable=False)
    email = sqla.Column(sqla.String(200), nullable=False)
    total_point = sqla.Column(sqla.Integer, nullable=False)  # a revoir
    etat = sqla.Column(sqla.String(200), nullable=False)  # a revoir present ou absent
    epreuves = db.relationship('Epreuve', secondary=evaluation, backref=db.backref('candidats'))
    copies = db.relationship('Copie', backref='candidat')
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)


class Centre(Updateable, db.Model):
    id = sqla.Column(sqla.String(200), primary_key=True)
    session = sqla.Column(sqla.String(200), nullable=False)  # annee
    nom_centre = sqla.Column(sqla.String(200), nullable=False)
    ia = sqla.Column(sqla.String(200), nullable=False)
    ief = sqla.Column(sqla.String(200), nullable=False)
    numero_jury = sqla.Column(sqla.String(200), nullable=False)  # apt ou inapte
    candidats = db.relationship('Candidat', secondary=affectation_candidat,
                                backref=db.backref('centres'))
    correcteurs = db.relationship('Correcteur',
                                  secondary=affectation_correcteur, backref=db.backref('centres'))
    membres_secretariat = db.relationship('MembreSecretariat',
                                          secondary=affectation_membre_secretariat, backref=db.backref('centres'))
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)


class Copie(Updateable, db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    note = sqla.Column(sqla.Integer, nullable=False)
    matiere = sqla.Column(sqla.String(200), nullable=False)
    candidat_id = db.Column(db.Integer, db.ForeignKey('candidat.id'), nullable=False)
    correcteur_id = db.Column(db.Integer, db.ForeignKey('correcteur.id'), nullable=False)


class Correcteur(Updateable, db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    copies = db.relationship('Copie', backref='correcteur')
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)



class Epreuve(Updateable, db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    libelle = sqla.Column(sqla.String(200), nullable=False)
    coefficient = sqla.column(sqla.Integer, nullable=False)
    type_epreuve = sqla.Column(sqla.String(200), nullable=False)  # 1er tour ou 2nd tour


class MembreSecretariat(Updateable, db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)
