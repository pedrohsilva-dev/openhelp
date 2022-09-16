from flask_wtf import FlaskForm
from wtforms import StringField, EmailField


class Teste(FlaskForm):
    teste = StringField('teste')
    campo = EmailField('campo')
