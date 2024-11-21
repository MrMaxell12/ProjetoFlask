from flask import Flask
from dynaconf import FlaskDynaconf
from extensions import db  # Importa o db do extensions.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tools.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Inicializa o db com o app

settings = FlaskDynaconf(
    app,
    settings_files=["settings.toml", ".secrets.toml"]
)


# Importar Blueprint
from routes.tool import tool_bp
app.register_blueprint(tool_bp)

# Rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)  # Modo de desenvolvimento, exibe erros no navegador
