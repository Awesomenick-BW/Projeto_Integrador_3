from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
import os
from flask_cors import CORS

# utilizando o flask
app = Flask(__name__)

# Aplicando o CORS
CORS(app)

# pegando o path do diretório
caminho = os.path.dirname(os.path.abspath(__file__))

# atribuindo lugar e nome do arquivobd
arquivobd = os.path.join(caminho, "banco_de_dados.db")

# configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)