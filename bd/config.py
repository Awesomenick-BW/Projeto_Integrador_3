from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
import os

# utilizando o flask
app = Flask(__name__)

# pegando o path do diretório
caminho = os.path.dirname(os.path.abspath(__file__))

# atribuindo lugar e nome do arquivobd
arquivobd = os.path.join(caminho, "usuario.db")

# configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)