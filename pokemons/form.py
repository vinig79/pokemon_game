from wtforms import BooleanField, SubmitField
from flask_wtf import FlaskForm

class Favorite(FlaskForm):
    set = BooleanField()
    submit = SubmitField("Submit")