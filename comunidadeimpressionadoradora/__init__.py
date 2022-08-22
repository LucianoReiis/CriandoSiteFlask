from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = 'fcda296a5bb64c9959ffe7bcf90fc253'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

from comunidadeimpressionadoradora import routes