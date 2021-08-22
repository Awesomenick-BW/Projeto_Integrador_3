"""No atual arquivo pode se localizar a classe Rascunho
que envia os dados para o banco de dados

Autor: Pedro Romig de Lima Souza.
"""
from config import *
from usuario import *
from aluno import *

# Classe responsável por criar um Rascunho
class Rascunho(db.Model):

    # Adicinando atibuto as variáveis
    # Definindo a variável 'id' como chave primária
    id = db.Column(db.Integer, primary_key="True")

    # Adicionando mais variáveis
    caracteres = db.Column(db.Integer)
    palavras = db.Column(db.Integer)
    titulo = db.Column(db.String(100))
    idAluno = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    
    """Método que define um caminho que é mais fácil de ler e mostrar 
    os outputs de todos os membros da classe"""
    def __str__(self):

        return str(self.caracteres) + ", " + str(self.palavras) + ", " + \
            self.titulo + ", " + str(self.idAluno)
    
    # Método responsável por printar o texto em formato json
    def json(self):

        return {
            "caracteres": self.caracteres,
            "palavras": self.palavras,
            "titulo": self.titulo,
            "idAluno": self.idAluno
        }


# Verificando se o diretório atual é o principal
if __name__ == "__main__":

    # Verificando se já existe um arquivo
    if os.path.exists(arquivobd):
        # Se a condição é verdadeira, remova o arquivo
        os.remove(arquivobd)

    # Criando tabelas
    db.create_all()

    # Instanciando um objeto
    nova = Rascunho(caracteres=1346, palavras=274, titulo="Socorro", idAluno=1)
    
    # Adicionando no banco de dados
    db.session.add(nova)
    db.session.commit()

    # Pegando os valores
    todas = db.session.query(Rascunho).all()

    # Laço de repetição necessário para imprimir os valores na tela
    for p in todas:
        print(p)
        print(p.json())