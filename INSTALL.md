# INSTALL seTUP PROJECT


## clone
git clone http://www.github.com/Pedro-ls/openhelp

## environment
python -m venv venv

## ENTRAR NO AMBIENTE
### cmd entrar no ambiente
.\venv\Scripts\activate

### powershell entrar no ambiente
.\venv\Scripts\Activate.ps1

## instalar dependencias
.\venv\Scripts\pip install -r requirements.txt

## copiar .env.example para .env
copy .env.example .env

## ARQUIVO .env

`
    // deletar linha de conexão postgres isso fará com que use sqlite por padrão.

    FLASK_ENV=development
    FLASK_DEBUG=1
    FLASK_APP=main.py
    PREFIX_URL=/prefix_url
`

## criar pastas necessarias
### pasta onde ficara banco de dados sqlite
mkdir temp
### pasta de upload de arquivos
mkdir files 

## cria banco sqlite
flask database create-tables

## run project
flask run

# MAIS COMANDOS UTEIS
## comando flask
`
    # mostra todos os comandos existentes dentro do flask
    flask
    # mostra todos os comandos de database
    flask database
`
## arquivo .env.
`
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_APP=main.py
PREFIX_URL=/prefix_url
`

