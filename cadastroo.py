from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CadastroForm(FlaskForm):
    username = StringField('Nome Usuário',validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    senha = PasswordField('Senha',validators=[DataRequired(), Length(min=4, max=20)])
    cadastrar = SubmitField('Cadastrar')
   