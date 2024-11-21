# Tenha certeza que a pasta aberta no vc é a pasta principal, o projeto tem que ter somente uma página raiz, geralmente chamada PROJETOFLASK/coisas aqui dentro


# Inicializar o ambiente pyhton

## Instalar o _virtualenv_
`pip install virtualenv`

## Iniciar o ambiente _venv_
`python -m venv .venv`

## Ativar o ambiente
Use 

`.venv/Scripts/activate.bat` para o CMD

ou

`.venv/Scripts/Activate.ps1` para o PowerShel

## Instar todas as dependências do projeto
`pip install -r requirements.txt`

# Rodar o app.py pelo menos uma vez para criar os arquivos .db

# Cria a pasta de migrações

`flask db init`   
`flask db migrate` 
`flask db upgrade` 

