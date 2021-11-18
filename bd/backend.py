from config import *
from usuario import Usuario
from aluno import Aluno
from professor import Professor

# Método para checar se o backend está operante
@app.route("/")
def padrao():
    return "backend operante"

# Método para listar pessoa
@app.route("/listar_usuarios")
def listar_usuarios():
    usuarios = db.session.query(Usuario).all()
    retorno = []
    for p in usuarios:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta

# Método para incluir pessoa
@app.route("/incluir_pessoa/<int:heranca>", methods=['post'])
def incluir_pessoa(heranca):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()

    try:
        if heranca == 1:
            nova = Professor(**dados)
        elif heranca == 2:
            nova = Aluno(**dados)
        
        db.create_all()
        db.session.add(nova)
        db.session.commit()

    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# teste: curl -X DELETE http://localhost:5000/excluir_pessoa/
# Método para excluir pessoa
@app.route("/excluir_pessoa/<int:pessoa_id>", methods=['DELETE'])
def excluir_pessoa(pessoa_id):
    resposta = jsonify({"resulatado": "ok", "detalhes": "ok"})

    try:
        Usuario.query.filter(Usuario.id == pessoa_id).delete()
        db.session.commit()
    except:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/encontrar_pessoa/", methods=['POST'])
def encontrar_pessoa():
    resposta = jsonify({"resultado": "erro", "detalhes": "erro ao validar"})
    dados = request.get_json()
    usuario = db.session.query(Usuario).filter(Usuario.email==dados["email"])
    if usuario.role == None:
        return "nada"
    elif usuario.role == "aluno":
        return "aluno"
    elif usuario.role == "professor":
        return "professor"
    else:
        return "nada"

app.run(debug = True)