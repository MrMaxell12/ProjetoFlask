from flask import Blueprint, render_template, request, redirect, url_for
from app import db  # Certifique-se de que o db é importado de app.py
from model.tool import Item  # Importa o modelo Item

tool_bp = Blueprint('tool', __name__)

# Rota para a página inicial, que exibe os itens
@tool_bp.route('/')
def index():
    items = Item.query.all()  # Consulta todos os itens no banco de dados
    return render_template('index.html', items=items)

# Rota para a página de adicionar item
@tool_bp.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])

        # Cria um novo item e adiciona ao banco de dados
        new_item = Item(nome=nome, preco=preco)
        db.session.add(new_item)
        db.session.commit()

        return redirect(url_for('tool.index'))  # Redireciona para a página principal

    return render_template('adicionar.html')

# Rota para remover um item
@tool_bp.route('/remover/<int:item_id>', methods=['GET', 'POST'])
def remover(item_id):
    item = Item.query.get_or_404(item_id)  # Encontra o item no banco

    if request.method == 'POST':
        nome_retirada = request.form.get('nome_retirada')  # Pega os dados do formulário
        cpf_retirada = request.form.get('cpf_retirada')

        # Verifica se os dados do formulário estão corretos
        if not nome_retirada or not cpf_retirada:
            return "Nome e CPF são obrigatórios", 400  # Retorna erro se dados não forem fornecidos
        
        # Atualiza o item no banco com as informações de retirada
        item.nome_retirada = nome_retirada
        item.cpf_retirada = cpf_retirada
        
        # Confirma a atualização no banco
        db.session.commit()

        # Após atualizar, podemos excluir o item
        db.session.delete(item)
        db.session.commit()

        return redirect(url_for('tool.index'))  # Redireciona para a página principal

    return render_template('remover.html', item=item)  # Exibe o formulário de remoção


