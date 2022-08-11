from email.policy import default
from enum import unique
from main import database
from datetime import datetime


class Usuario(database.Model):
    id = database.column(database.Integer, primary_key=True)
    username = database.column(database.String, nullable=False)
    email = database.column(database.String, nullable=False, unique=True)
    senha = database.column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não informado')



class Post(database.Model):
    id = database.column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)