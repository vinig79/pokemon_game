from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(),Email()])
    submit = SubmitField("Submit")

class ResgistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired(), Email()])
    email2 = StringField('email',validators=[DataRequired(), Email(),EqualTo('email')])
    subimit = SubmitField("Submit")