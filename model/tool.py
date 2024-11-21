from extensions import db  # Importa o db configurado

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    nome_retirada = db.Column(db.String(100), nullable=True)
    cpf_retirada = db.Column(db.String(14), nullable=True)

    def __repr__(self):
        return f"<Item {self.nome}>"
