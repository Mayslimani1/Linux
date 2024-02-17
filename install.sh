#!/bin/bash

virtualenv venv

source ./venv/bin/activate

#Installer kaggle
pip install kaggle

# Installer les dépendances Python via pip
pip install -r requirements.txt

# Installation de Streamlit
pip install streamlit

# Assurez-vous que votre script est exécutable
chmod +x install.sh