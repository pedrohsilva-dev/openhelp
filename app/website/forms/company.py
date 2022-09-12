from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class Company(Form):
    fantasy_name = StringField('Nome fantasia')
    email = StringField('E-mail')
    password = PasswordField('Senha')
    city = StringField('Cidade')
    state = StringField('Estado')
    cnpj = StringField('CNPJ')


class CompanyLogin(Form):
    email = StringField('email')
    password = PasswordField('password')
