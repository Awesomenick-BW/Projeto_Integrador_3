from config import *
from usuario import Usuario
from aluno import Aluno

@app.route("/")
def padrao():
    return "backend operante"

@app.route("/listar_usuarios")
def listar_usuarios():
    usuarios = db.session.query(Usuario).all()
    retorno = []
    for p in usuarios:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    return resposta

app.run(debug = True)