#!/bin/bash

virtualenv venv

source ./venv/bin/activate

# Installer les dépendances
python3 -m pip install kaggle
python3 -m pip install pandas
python3 -m pip install base64
python3 -m pip install streamlit
pip -r requirements.txt

# Assurez-vous que votre script est exécutable
chmod +x install.sh