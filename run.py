from app import create_app, db
from app.models import Tarefa

# Criação da instância da aplicação
app = create_app()

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)