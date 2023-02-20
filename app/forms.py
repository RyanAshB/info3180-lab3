from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), email()])
    subject = StringField('Subject', validators=[InputRequired()])
    message = TextAreaField('Message', validators = [InputRequired()])
    