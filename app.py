from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email, senha):
        self.username = username
        self.email = email
        self.senha = generate_password_hash(senha)




db.create_all()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

if(__name__ == '__main__'):
    app.run(debug=True)