echo "Virtualenv create"

python3 -m venv venv

sleep 1

echo "Entrar Virtualenv"
.\venv\Scripts\Activate.ps1

sleep 1

echo "PIP install requirements"
.\venv\Scripts\pip3 --proxy="" install -r requirements.txt

sleep 1

echo "copy .env.example to .env"
cp .env.example .env

echo "Finished"