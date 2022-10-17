from app import db

Pok_tipo = db.Table('Pok_tipo', db.metadata, db.Column("id_pok", db.Integer, db.ForeignKey("Pokemon.id_pok")),db.Column('id_tipo', db.Integer, db.ForeignKey('Tipo.id_tipo')))
user_pok = db.Table('user_pok', db.metadata, db.Column("id_user", db.Integer, db.ForeignKey('Usuario.id_user')), db.Column('id_pok', db.Integer, db.ForeignKey('Pokemon.id_pok')))

class Pokemon(db.Model):
    id_pok = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    atk = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    atk_special = db.Column(db.Integer, nullable=False)
    special_defense = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    tipo = db.relationship("Tipo", secondary=Pok_tipo)

class Tipo(db.Model):
    id_tipo = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(150), nullable=False)

class Usuario(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    raking = db.relationship('Ranking', uselist=False, back_populates='usuario')

class Rankin(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey("Usuario.id_user"), primary_key=True)
    position = db.Column(db.Integer, nullable=False)
    vitorias = db.Column(db.Integer, nullable=False)
    usuario = db.relationship("Usuario",back_populates="ranking")

class Local_(db.Model):
    id_local = db.Column(db.Integer, primary_key=True)
    local_ = db.Column(db.String(150), nullable=False)

class Torneio(db.Model):
    id_torneio = db.Column(db.Integer, primary_key=True)
    id_local = db.Column(db.Integer,db.ForeignKey("Local_.id_local"), nullable=False)
    nome = db.Column(db.String(150), nullable=False)
    medalha = db.relationship('Medalha')


class Medalha(db.Model):
    medal_id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("Usuario.id_user"))
    nome = db.Column(db.String(150), nullable=False)
    id_torneio = db.Column(db.Integer, db.ForeignKey("Torneio.id_torneio"))