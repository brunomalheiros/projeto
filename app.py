from flask import Flask, render_template, redirect, url_for,session
from flask_sqlalchemy import SQLAlchemy
from cadastroo import CadastroForm
from login import LoginForm
from denuncia import DenunciaForm
from flask_login import LoginManager, login_user, logout_user


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SECRET_KEY'] = 'chavinha'
db = SQLAlchemy(app)
login_manager = LoginManager(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    senha = db.Column(db.String(80), nullable = False)
    denuncia = db.relationship('Denuncia', backref='usuario', lazy=True)


    def __init__(self, username, email, senha):
        self.username = username
        self.email = email
        self.senha = senha

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)
    
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.filter_by(id=user_id).first()

class Denuncia(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    usuario_id = db.Column(
        db.Integer, 
        db.ForeignKey('usuario.id'), 
        nullable=False
    )  

db.create_all()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/denuncia',methods=['GET', 'POST'])
def denuncia():

    form = DenunciaForm()
    if form.validate_on_submit():
        denun = Denuncia()
        denun.usuario_id = 1
        denun.titulo = form.titulo.data
        denun.conteudo = form.conteudo.data
        db.session.add(denun)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('denuncia.html', form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user and user.senha == form.senha.data:
            login_user(user)
            return redirect(url_for('home'))

    return render_template('login.html', form=form)
    
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        user = Usuario(form.username.data, form.email.data, form.senha.data)
        db.session.add(user)
        db.session.commit()
        return redirect (url_for('home'))


    return render_template('cadastro.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    logout_user()   
    return redirect(url_for('home'))

if(__name__ == '__main__'):
    app.run(debug=True)