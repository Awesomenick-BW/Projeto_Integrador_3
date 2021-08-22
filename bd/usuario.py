"""No atual arquivo pode se localizar a classe Usuario
que envia os dados para o banco de dados

Autores: Braian Wandelan, Daniel Krüger e Pedro Romig de Lima Souza.
"""
from config import *

# Classe responsável por adicionar atributos no banco de dados
class Usuario(db.Model):

    # Adicinando as variáveis ao banco de dados
    # Definindo a variável 'id' como chave primária
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(25))
    cpf = db.Column(db.String(15))
    email = db.Column(db.String(25))
    idade = db.Column(db.Integer)

    # Definindo um coluna que irá mostrar se for filho ou pai
    type = db.Column(db.String(50))

    # Definindo Usuario como pai da herança
    __mapper_args__ = {
        'polymorphic_identity':'usuario',
        'polymorphic_on':type
    }
    
    # 
    def __str__(self):
        return str(self.id) + "," + self.nome + ", " + self.cpf + ", " + \
            self.email + ", " + str(self.idade)
    
    def json(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "cpf" : self.cpf,
            "idade" : self.idade
        }


if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    nova = Usuario(nome="Daniel", cpf="777.777.777.77", email="alas@gmail.com", idade=18)
    
    db.session.add(nova)
    db.session.commit()
    todas = db.session.query(Usuario).all()
    for p in todas:
        print(p)
        print(p.json())
    # print(nova.nome)