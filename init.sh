#!/bin/bash

echo "Virtualenv create"
python3 -m venv venv

echo "Entrar Virtualenv"
source ./venv/bin/activate

echo "PIP install requirements"
./venv/bin/pip3 --proxy="" install -r requirements.txt

echo "Installed..."

echo "copy .env.example to .env"
cp .env.example .env

echo "Finished"
