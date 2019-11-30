from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CadastroForm(FlaskForm):
    username = StringField('Nome de usuário',validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    senha = PasswordField('Senha',validators=[DataRequired(), Length(min=8, max=80)])
    cadastrar = SubmitField('Cadastrar')
   