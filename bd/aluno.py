"""No atual arquivo pode se localizar a classe Aluno
que envia os dados para o banco de dados

Autor: Daniel Krüger.
"""
from config import *
from usuario import *

# Classe responsável por criar um Aluno
class Aluno(Usuario):

    # Adicinando atibuto as variáveis
    # Definindo a variável 'id' como chave primária
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key="True")
    
    # Definindo que Aluno é filho de uma classe pai
    __mapper_args__ = {
        'polymorphic_identity':'aluno'
    }

    # Adicionando mais variáveis
    escolaridade = db.Column(db.String(50))
    materias_fracas = db.Column(db.String(50))
    objetivo = db.Column(db.String(100))
    
    """Método que define um caminho que é mais fácil de ler e mostrar 
    os outputs de todos os membros da classe"""
    def __str__(self):
        # Utilizando o super() para herdar o método
        return super().__str__() + ", " + self.escolaridade + \
            ", " + self.materias_fracas + ", " + self.objetivo
    
    # Método responsável por printar o texto em formato JavaScript
    def json(self):
        # Utilizando o super() para herdar o método
        return super().json() | {
            "escolaridade": self.escolaridade,
            "materias_fracas": self.materias_fracas,
            "objetivo": self.objetivo
        }


# Verificando de o diretório atual é o principal
if __name__ == "__main__":

    # Verificando de já existe um arquivo
    if os.path.exists(arquivobd):
        # Removendo o arquivo
        os.remove(arquivobd)

    # Criando tabelas
    db.create_all()

    # Instanciando um objeto
    nova = Aluno(nome="Roberto", cpf="888.888.888.88", email="opa@gmail.com", idade=19, 
    escolaridade="ensino médio completo", materias_fracas="port", objetivo="sobreviver")
    
    # Adicionando no bd
    db.session.add(nova)
    db.session.commit()

    # Pegando os valores
    todas = db.session.query(Aluno).all()

    # Laço de repetição necessário para mostrar na tela os valores
    for p in todas:
        print(p)
        print(p.json())