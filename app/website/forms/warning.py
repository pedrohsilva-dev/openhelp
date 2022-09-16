from flask_wtf import FlaskForm as Form
from wtforms import StringField, FileField, TextAreaField
from wtforms.validators import DataRequired


class WarningForm(Form):
    title = StringField('titulo')
    content = TextAreaField('conteudo')
    photo = FileField('foto do Aviso')
