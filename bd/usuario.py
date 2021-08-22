"""No atual arquivo pode se localizar a classe Usuario
que envia os dados para o banco de dados

Autores: Braian Wandelan, Daniel Krüger e Pedro Romig de Lima Souza.
"""
from config import *

# Classe responsável por criar um Usuário
class Usuario(db.Model):

    # Adicinando atributo as variáveis
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
    
    """Método que define um caminho que é mais fácil de ler e mostrar 
    os outputs de todos os membros da classe"""
    def __str__(self):
        return str(self.id) + "," + self.nome + ", " + self.cpf + ", " + \
            self.email + ", " + str(self.idade)
    
    # Método responsável por printar o texto em formato JavaScript
    def json(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "cpf" : self.cpf,
            "idade" : self.idade
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
    nova = Usuario(nome="Alberto", cpf="777.777.777.77", email="alas@gmail.com", idade=18)
    
    # Adicionando no bd
    db.session.add(nova)
    db.session.commit()

    # Pegando os valores
    todas = db.session.query(Usuario).all()

    # Laço de repetição necessário para mostrar na tela os valores
    for p in todas:
        print(p)
        print(p.json())