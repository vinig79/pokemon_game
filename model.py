from pokemon import db

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