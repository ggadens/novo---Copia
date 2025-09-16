from app import db  # Importa o db corretamente

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chave primária
    descricao = db.Column(db.String(120), unique=True, nullable=False)  # Descrição da tarefa

    def __repr__(self):
        return f'<Tarefa {self.descricao}>'