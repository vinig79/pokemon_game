from pokemon import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from pokemon import login_manager


Pok_tipo = db.Table("Pok_tipo", db.metadata,
                     db.Column("id_pok", db.ForeignKey("pokemon.id_pok"), primary_key=True),
                     db.Column("id_tipo", db.ForeignKey("tipo.id_tipo"), primary_key=True)
                     )

User_pok = db.Table("User_pok",db.metadata,
                    db.Column("id_pok", db.ForeignKey("pokemon.id_pok"), primary_key=True),
                    db.Column("id_user", db.ForeignKey("user.id_user"), primary_key=True)
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
    id_user = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    favorite = db.relationship("Pokemon", secondary=User_pok, backref="pokemon")


    def is_favorite(self, pokemon):
        if not pokemon in self.favorite:
            return True
        return False
    def favoritar(self, pokemon):
        self.favorite.append(pokemon)

    def desfavoritar(self, pokemon):
        self.favorite.remove(pokemon)
    def get_id(self):
        return self.id_user
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
