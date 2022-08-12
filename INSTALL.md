# INSTALL SETUP PROJECT


## clone do projeto
```bash
git clone http://www.github.com/Pedro-ls/openhelp
```
-----------------------------
## environment
```bash
python -m venv venv
```
## ENTRAR NO AMBIENTE
### UNIX entrar no ambiente
```bash
# no lugar de source pode-se usas "."
source ./venv/bin/activate
# . ./venv/bin/activate
```
### cmd entrar no ambiente
```cmd
.\venv\Scripts\activate
```
### powershell entrar no ambiente
```powershell
.\venv\Scripts\Activate.ps1
```
-----------------------------
## instalar dependencias

### Unix
```bash
./venv/bin/pip install -r requirements.txt
```
### Windows
```cmd
.\venv\Scripts\pip install -r requirements.txt
```
-----------------------------
## copiar .env.example para .env
### Unix
```bash
cp .env.example .env
```
### Windows
```cmd
copy .env.example .env
```
-----------------------------
## ARQUIVO .env
```python
# deletar linha de conexão postgres isso fará com que use sqlite por padrão.

FLASK_ENV=development
FLASK_DEBUG=1
FLASK_APP=main.py
PREFIX_URL=/prefix_url
```
-----------------------------
## criar pastas necessarias
### pasta onde ficara banco de dados sqlite
```bash
mkdir temp
```
### pasta de upload de arquivos
```bash
mkdir files
```
-----------------------------
## cria banco sqlite
```bash
flask database create-tables
```
## run project
```bash
flask run
```

# MAIS COMANDOS UTEIS
## comando flask

#### Mostra todos os comandos existentes dentro do flask
```bash
    flask
```
#### Mostra todos os comandos de database
```bash
    flask database
```

## arquivo .env.
```python
# arquivo ".env" - obrigatório 

SQLALCHEMY_DATABASE_URI=postgresql://user:password/database # URL postgresql apague ela caso queira usar sqlite
FLASK_ENV=development # setando ambiente de desenvolvimento
FLASK_DEBUG=1 # modo debug ou não  - 0 desativado e 1 ativado
FLASK_APP=main.py # arquivo principal
PREFIX_URL=/api # prefixo da API
```

## CASO INSTALAR NOVA BIBLIOTECA RODAR COMANDO
### UNIX
```bash
./venv/bin/pip freeze >> requirements.txt
```
### WINDOWS
### UNIX
```cmd
.\venv\Scripts\pip freeze >> requirements.txt
```
