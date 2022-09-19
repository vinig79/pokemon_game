from app import db

class Player(db.Model):    
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    # Pokemon FK here

class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30))
    tipo = db.Column(db.String(15))
    # Pokemon Status FK here

class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    ataque = db.Column(db.Integer)
    defesa = db.Column(db.Integer)
    velocidade = db.Column(db.Integer)
    vida = db.Column(db.Integer)