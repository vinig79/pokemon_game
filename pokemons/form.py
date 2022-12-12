from wtforms import BooleanField, SubmitField
from flask_wtf import FlaskForm

class Favorite(FlaskForm):
    favoritar = SubmitField("Favoritar")
    desfavoritar = SubmitField("Desfavoritar")