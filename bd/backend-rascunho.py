from config import *
from rascunho import Rascunho

# Checar se o Backend está operante
@app.route("/")
def padrao():
    return "backend operante"

# Lista o número de rascunhos e seus dados
@app.route("/listar_rascunhos")
def listar_usuarios():
    rascunhos = db.session.query(Rascunho).all()
    retorno = []
    for p in rascunhos:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    return resposta

# Inclui um rascunho - !! Em fase de Testes !!
@app.route("/incluir_rascunho", methods=['post'])
def incluir_rascunho():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()

    try:
        novo = Rascunho(**dados)

        db.create_all()
        db.session.add(nova)
        db.session.commit()

    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    resposta.headers.add("Access-control-Allow-Origin", "*")
    return resposta

app.run(debug = True)