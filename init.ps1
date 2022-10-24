echo "Virtualenv create"
python3 -m venv venv
echo "create folder files"
mkdir files
echo "create folder temp"
mkdir temp
echo "PIP install requirements"
.\venv\Scripts\pip3 --proxy="" install -r requirements.txt
echo "copy .env.example to .env"
cp .env.example .env
echo "Desbloqueie as permissões de comandos do powershell"
echo "Rode os codigos no powershell"
echo ""
echo "powershell"
echo ".\venv\Scripts\Activate.ps1"
echo "CMD"
echo ".\venv\Scripts\activate"
echo ""
echo ""
echo "flask create-tables"
echo ""
echo ""
echo "flask run"
