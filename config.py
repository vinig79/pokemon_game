import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI =  'mysql+mysqlconnector://vinig79:vinig79@localhost/pokemon_game'
    SQLALCHEMY_TRACK_MODIFICATIONS = False