from config import *
from rascunho import Rascunho

@app.route("/")
def padrao():
    return "backend operante"

@app.route("/listar_rascunhos")
def listar_usuarios():
    rascunhos = db.session.query(Rascunho).all()
    retorno = []
    for p in rascunhos:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    return resposta

app.run(debug = True)