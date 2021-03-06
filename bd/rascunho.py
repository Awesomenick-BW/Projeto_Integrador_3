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
    titulo = db.Column(db.String(30))
    texto = db.Column(db.String(4000))
    comentario = db.Column(db.String(500))
    emailAluno = db.Column(db.String(20))
    
    """Método que define um caminho que é mais fácil de ler e mostrar 
    os outputs de todos os membros da classe"""
    def __str__(self):

        return self.texto + ", " + str(self.idAluno)
    
    # Método responsável por printar o texto em formato json
    def json(self):

        return {
            "titulo": self.titulo,
            "texto": self.texto,
            "comentario": self.comentario,
            "emailAluno": self.emailAluno
        }