from config import *
from usuario import Usuario
from aluno import Aluno
from professor import Professor
from rascunho import Rascunho

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
        # Filtro na tabela para identificar a pessoa, para assim deletá-la
        Usuario.query.filter(Usuario.id == pessoa_id).delete()
        Aluno.query.filter(Aluno.id == pessoa_id).delete()
        Professor.query.filter(Professor.id == pessoa_id).delete()
        
        db.session.commit()

    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# curl -d '{"email":"jo@gmail.com", "senha":"123"}' -X POST -H "Content-Type:application/json" localhost:5000/encontrar_pessoa
# Método para encontrar pessoa
@app.route("/encontrar_pessoa", methods=['POST'])
def encontrar_pessoa():
    dados = request.get_json()
    aluno = db.session.query(Aluno).filter(Aluno.email==dados["email"] and Aluno.senha==dados["senha"]).first()
    professor = db.session.query(Professor).filter(Professor.email==dados["email"] and Professor.senha==dados["senha"]).first()

    # Verificação para identificar se as instâncias estão vazias
    if aluno != None:
        value = "aluno"
        email = aluno.email # Enviando email do aluno e a role do mesmo
    elif professor != None:
        value = "professor"
        email = professor.email # Enviando o email do professor e a role do mesmo
    else:
        value = "nada"
    
    resposta = jsonify({"resultado": value, "email": email})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# curl -d '{"id": 1, "idade": 20, "role": "aluno"}' -X POST -H "Content-Type:application/json" localhost:5000/update
# Método de UPDATE
@app.route("/update", methods=["POST"])
def editar_aluno():
    dados = request.get_json()
    resposta = jsonify({"resulatado": "ok", "detalhes": "ok"})

    try:
        # Verificando se o role passado é da respectiva pessoa
        if dados["role"] == "aluno":
            novo = db.session.query(Aluno).filter(Aluno.id == dados['id']).first()

            # Atualizando os dados campo por campo
            for key in dados:
                setattr(novo, key, dados[key])

            db.session.commit()
        elif dados["role"] == "professor":
            novo = db.session.query(Professor).filter(Professor.id == dados['id']).first()

            for key in dados:
                setattr(novo, key, dados[key])

            db.session.commit()

    except Exception as e:
        resposta = jsonify({"resulatado": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# Apartir daqui são métodos desenvolviemdos para a Redação

# Lista o número de rascunhos e seus dados
@app.route("/listar_rascunhos")
def listar_rascunhos():
    rascunhos = db.session.query(Rascunho).all()
    retorno = []
    for p in rascunhos:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    return resposta

# curl -d '{"titulo": "Sua mãe", "texto":"123", "comentario": "nenhum", "emailAluno": "abac@gmail.com"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_rascunho
# Inclui um rascunho
@app.route("/incluir_rascunho", methods=['post'])
def incluir_rascunho():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()

    try:
        novo = Rascunho(**dados)

        db.create_all()
        db.session.add(novo)
        db.session.commit()

    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    resposta.headers.add("Access-control-Allow-Origin", "*")
    return resposta

# curl -d '{"titulo": "Sua mãe", "comentario": "nenhum", "emailAluno": "abac@gmail.com"}' -X POST -H "Content-Type:application/json" localhost:5000/update_rascunho
# Método UPDATE para a redação
@app.route("/update_rascunho", methods=['post'])
def update_rascunho():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()

    try:
        novo = db.session.query(Rascunho).filter(Rascunho.emailAluno == dados['emailAluno'] and Rascunho.titulo == dados['titulo']).first()

        """for key in dados:
            setattr(novo, key, dados[key])"""
        novo.comentario = dados['comentario']

        db.session.commit()

    except Exception as e:
        resposta = jsonify({"resulatado": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/rascunho_aluno", methods=['post'])
def rascunho_aluno():
    dados = request.get_json()

    rascunhos = db.session.query(Rascunho).filter(Rascunho.emailAluno == dados['email']).all()
    retorno = []
    for p in rascunhos:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    return resposta

app.run(debug = True)
