#!/bin/bash

# Activation de l'environnement virtuel
source .venv/bin/activate

# Définir le répertoire de configuration Kaggle
export KAGGLE_CONFIG_DIR=data_collector/.kaggle

# Téléchargement de l'ensemble de données Kaggle dans le répertoire "data"
kaggle datasets download -d airbnb/seattle

# Création du répertoire "data" s'il n'existe pas
mkdir -p data

# Déplacement du fichier téléchargé dans le répertoire "data"
mv "seattle.zip" data/
unzip data/seattle.zip

# Accorder des permissions au répertoire "data"
chmod -R 777 data

echo "Téléchargement et déplacement terminés"
