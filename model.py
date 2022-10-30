from pokemon import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from pokemon import login

Pok_tipo = db.Table("Pok_tipo", db.metadata,
                     db.Column("id_pok", db.ForeignKey("pokemon.id_pok"), primary_key=True),
                     db.Column("id_tipo", db.ForeignKey("tipo.id_tipo"), primary_key=True)
                     )


class Pokemon(db.Model):
    id_pok = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    atk = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    atk_special = db.Column(db.Integer, nullable=False)
    special_defense = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    tipos = db.relationship("Tipo",secondary=Pok_tipo, backref="pokemons")


class Tipo(db.Model):
    id_tipo = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(150), nullable=False)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))