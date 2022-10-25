from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from model import User

class Login(FlaskForm):
    nome = StringField('nome',validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField("submit")

class Register(FlaskForm):
    nome = StringField('nome',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired(),Email()])
    email2 = StringField('email',validators=[DataRequired(),EqualTo('email')])
    submit = SubmitField("Register")

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("use other email")