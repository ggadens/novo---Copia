from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Tarefa

# Criação do Blueprint 'hello'
hello_bp = Blueprint('hello', __name__)

# Rota para a página principal (Listar, Criar e Excluir tarefas)
@hello_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        descricao = request.form['descricao']

        # Verifica se a tarefa já existe (unique constraint)
        tarefa_existente = Tarefa.query.filter_by(descricao=descricao).first()
        if tarefa_existente:
            return render_template('index.html', tarefas=Tarefa.query.all(), erro="Tarefa já existe.")  # Exibe um erro

        nova_tarefa = Tarefa(descricao=descricao)
        db.session.add(nova_tarefa)
        db.session.commit()  # Confirma a transação

    tarefas = Tarefa.query.all()  # Recupera todas as tarefas do banco de dados
    return render_template('index.html', tarefas=tarefas)

# Rota para editar uma tarefa
@hello_bp.route('/editar_tarefa/<int:tarefa_id>', methods=['GET', 'POST'])
def editar_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)  # Busca a tarefa pelo ID
    
    if request.method == 'POST':
        tarefa.descricao = request.form['descricao']  # Atualiza a descrição da tarefa
        db.session.commit()  # Confirma a alteração
        return redirect(url_for('hello.index'))  # Redireciona para a página principal

    return render_template('editar_tarefa.html', tarefa=tarefa)  # Exibe o formulário de edição com a tarefa

# Rota para excluir uma tarefa
@hello_bp.route('/deletar_tarefa/<int:tarefa_id>', methods=['POST'])
def deletar_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)  # Busca a tarefa pelo ID
    db.session.delete(tarefa)  # Deleta a tarefa
    db.session.commit()  # Confirma a exclusão
    return redirect(url_for('hello.index'))  # Redireciona para a página principal