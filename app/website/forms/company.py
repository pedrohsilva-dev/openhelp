from flask_wtf import FlaskForm as Form
from wtforms import StringField, EmailField, PasswordField, FileField
from wtforms.validators import DataRequired


class Company(Form):
    fantasy_name = StringField('Nome fantasia')
    email = EmailField('E-mail')
    password = PasswordField('Senha')
    city = StringField('Cidade')
    state = StringField('Estado')
    cnpj = StringField('CNPJ')
    photo = FileField("photo")


class CompanyLogin(Form):
    email = StringField('email')
    password = PasswordField('password')
