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
        id_ = aluno.id # Enviando id do aluno e a role do mesmo
    elif professor != None:
        value = "professor"
        id_ = professor.id # Enviando id do aluno e a role do mesmo
    else:
        value = "nada"
    
    resposta = jsonify({"resultado": value, "identificador": id_})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# curl -d '{"id": 1, "nome": "abacate", "cpf": "123.456.789-10", "email":"abac@gmail.com", "senha":"123", "idade": 20}' -X POST -H "Content-Type:application/json" localhost:5000/update/
# Método de UPDATE
@app.route("/update/<int:role>", methods=["POST"])
def editar_aluno(role):
    dados = request.get_json()
    resposta = jsonify({"resulatado": "ok", "detalhes": "ok"})

    try:
        # Verificando se o role passado é da respectiva pessoa
        if role == 1:
            novo = db.session.query(Aluno).filter(Aluno.id == dados['id']).first()

            # Atualizando os dados campo por campo
            novo.nome = dados['nome']
            novo.email = dados['email']
            novo.cpf = dados['cpf']
            novo.idade = dados['idade']
            novo.senha = dados['senha']

            db.session.commit()
        elif role == 2:
            novo = db.session.query(Professor).filter(Professor.id == dados['id']).first()

            novo.nome = dados['nome']
            novo.email = dados['email']
            novo.cpf = dados['cpf']
            novo.idade = dados['idade']
            novo.senha = dados['senha']

            db.session.commit()

    except Exception as e:
        resposta = jsonify({"resulatado": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug = True)
