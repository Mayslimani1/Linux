#!/bin/bash

# Activation de l'environnement virtuel
#source .venv/bin/activate
pip install kaggle
sudo apt-get install unzip

# Définir le répertoire de configuration Kaggle
export KAGGLE_CONFIG_DIR=kaggle

# Téléchargement de l'ensemble de données Kaggle
kaggle datasets download -d polartech/16000-grab-restaurants-in-singapore
echo "Téléchargement terminé"

#Création du dossier data
mkdir -p data

# Déplacement du fichier téléchargé dans le répertoire data
mv "16000-grab-restaurants-in-singapore.zip" data/
unzip -o 16000-grab-restaurants-in-singapore.zip -d data/
echo "Dossier dézipé"

mv "Grab SG Restaurants.csv" "Grab_SG_Restaurants.csv"
mv "Grab_SG_Restaurants.csv" data/
echo "Bases sauvegardées dans data"

# Accorder des permissions au répertoire data
chmod +x data

