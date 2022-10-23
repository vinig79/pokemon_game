class Config(object):
    DEBUG = TESTING = True
    DATABASE_URI = "mysql+mysqlconnector://vinig79:vinig79@localhost/POKEMON_GAME"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
