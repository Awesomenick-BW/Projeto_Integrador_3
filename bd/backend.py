from config import *
from usuario import Usuario
from aluno import Aluno
from professor import Professor

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
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta

@app.route("/incluir_pessoa", methods=['post'])
def incluir_pessoa():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()

    try:
        nova = Usuario(**dados)
        db.session.add(nova)
        db.session.commit()
    
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug = True)