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
    texto = db.Column(db.String(4000))
    idAluno = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    
    """Método que define um caminho que é mais fácil de ler e mostrar 
    os outputs de todos os membros da classe"""
    def __str__(self):

        return self.texto + ", " + str(self.idAluno)
    
    # Método responsável por printar o texto em formato json
    def json(self):

        return {
            "texto": self.texto,
            "idAluno": self.idAluno
        }