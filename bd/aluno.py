from config import *
from usuario import *

class Aluno(Usuario):
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key="True")

    __mapper_args__ = {
        'polymorphic_identity':'aluno'
    }

    escolaridade = db.Column(db.String(50))
    materias_fracas = db.Column(db.String(50))
    objetivo = db.Column(db.String(100))
    
    def __str__(self):
        return super().__str__() + ", " + self.escolaridade + ", " + self.materias_fracas + \
            ", " + self.objetivo
    
    def json(self):
        return super().json() | {
            "escolaridade": self.escolaridade,
            "materias_fracas": self.materias_fracas,
            "objetivo": self.objetivo
        }


if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    nova = Aluno(nome="Daniel", cpf="777.777.777.77", email="alas@gmail.com", idade=18, 
    escolaridade="ensino médio completo", materias_fracas="port", objetivo="sobreviver")
    
    db.session.add(nova)
    db.session.commit()
    todas = db.session.query(Aluno).all()
    for p in todas:
        print(p)
        print(p.json())
    # print(nova.nome)