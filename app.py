from flask import Flask
from dynaconf import FlaskDynaconf
from flask_migrate import Migrate
from extensions import db  # Importa o db configurado no extensions.py

# Criação do app
app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tools.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o db com o app
db.init_app(app)

# Configuração do Migrate
migrate = Migrate(app, db)

# Configuração do Dynaconf
settings = FlaskDynaconf(
    app,
    settings_files=["settings.toml", ".secrets.toml"]
)

# Importa Blueprint
from routes.tool import tool_bp
app.register_blueprint(tool_bp)

# Rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)
