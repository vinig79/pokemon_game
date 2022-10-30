from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class Login(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")
    submit = SubmitField("submit")
