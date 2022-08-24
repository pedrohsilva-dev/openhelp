#!/bin/bash

echo "Virtualenv create"
python3 -m venv venv

sleep 1

echo "Entrar Virtualenv"
source ./venv/bin/activate

sleep 1

echo "PIP install requirements"
./venv/bin/pip3 --proxy="" install -r requirements.txt

sleep 1

echo "copy .env.example to .env"
cp .env.example .env

echo "Finished"