from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class DenunciaForm(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    conteudo = StringField('Conteudo', validators=[DataRequired()])
    enviar = SubmitField('Enviar Denuncia')