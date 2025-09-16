from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa o objeto db globalmente
db = SQLAlchemy()

def create_app():
    # Inicializa a instância do Flask
    app = Flask(__name__)

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Associa o db com a aplicação
    db.init_app(app)

    # Importa e registra o blueprint 'hello' após a configuração do db
    from .hello.routes import hello_bp
    app.register_blueprint(hello_bp)

    return app