#!/bin/bash

virtualenv venv

source ./venv/bin/activate

# Installer les dépendances
pip install --upgrade pip
pip install kaggle pandas base64 streamlit -r requirements.txt

# Assurez-vous que votre script est exécutable
chmod +x install.sh