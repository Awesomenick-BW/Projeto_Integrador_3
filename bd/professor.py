"""No atual arquivo pode se localizar a classe Professor
que envia os dados para o banco de dados

Autor: Braian Wandalen.
"""
from config import *
from usuario import *

# Classe responsável por criar um Professor
class Professor(Usuario):

    # Adicinando atibuto as variáveis
    # Definindo a variável 'id' como chave primária
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key="True")

    # Definindo que Professor é filho de uma classe pai
    __mapper_args__ = {
        'polymorphic_identity':'professor'
    }

    # Adicionando um identificador de Professor
    role = db.Column(db.String(10))
    
    """Método que define um caminho que é mais fácil de ler e mostrar 
    os outputs de todos os membros da classe"""
    def __str__(self):
        # Utilizando o super() para herdar o método
        return super().__str__() + ", " + self.role
    
    # Método responsável por printar o texto em formato json
    def json(self):
        json1 = super().json()
        json2 = json1.update({"role": self.role})

        return json1