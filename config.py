import os
class Config(object):
    DEBUG = TESTING = True
    DATABASE_URI = "mysql+mysqlconnector://vinig79:vinig79@localhost/POKEMON_GAME"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SECRET_KEY = os.environ.get("SECRET_KEY") or  "you-will-never-guess"