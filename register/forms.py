from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from model import User

class Register(FlaskForm):
    nome = StringField('name',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired(),Email()])
    password_1 = StringField('password',validators=[DataRequired()])
    password_2 = StringField('repeat password', validators=[DataRequired(), EqualTo('password_1')])
    submit = SubmitField("Register")

    def validate_email(self,email):
        user = User.query.filter_by(email= email.data).first()
        if user is not None:
            raise ValidationError("use other email")