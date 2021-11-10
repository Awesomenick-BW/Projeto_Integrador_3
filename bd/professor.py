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

    """
    # Adicionando mais variáveis
    area_de_atuacao = db.Column(db.String(75))
    formacao = db.Column(db.String(150))
    experiencia = db.Column(db.String(100))
    """
    
    """Método que define um caminho que é mais fácil de ler e mostrar 
    os outputs de todos os membros da classe"""
    def __str__(self):
        # Utilizando o super() para herdar o método
        return super().__str__() + ", " + self.area_de_atuacao + \
            ", " + self.formacao + ", " + self.experiencia
    
    # Método responsável por printar o texto em formato json
    def json(self):
        json1 = super().json()
        json2 = json1.update({
            "area_de_atuacao": self.area_de_atuacao,
            "formacao": self.formacao,
            "experiencia": self.experiencia
        })

        return json1

# Verificando se o diretório atual é o principal
if __name__ == "__main__":
    # Criando tabelas
    db.create_all()

    # Instanciando um objeto
    nova = Professor(nome="Henrique", cpf="111.111.111.11", email="henrique_prof@gmail.com", idade=37, 
    area_de_atuacao="linguagem, letras, enem", formacao="bacharelado em letras", experiencia="15 anos de atuacao em ensino medio e superior")
    
    # Adicionando no banco de dados
    db.session.add(nova)
    db.session.commit()

    # Pegando os valores
    todas = db.session.query(Professor).all()

    # Laço de repetição necessário para mostrar na tela os valores
    for p in todas:
        print(p)
        print(p.json())