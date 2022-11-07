from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired


class Login(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")
    submit = SubmitField("submit")
