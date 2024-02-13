#!/bin/bash

# Activation de l'environnement virtuel
source .venv/bin/activate

# Définir le répertoire de configuration Kaggle
export KAGGLE_CONFIG_DIR=data_collector/.kaggle

# Téléchargement de l'ensemble de données Kaggle
kaggle datasets download -d tejpal123/human-disease-prediction-dataset
echo "Téléchargement terminé"

#Création du dossier data
mkdir -p data

# Déplacement du fichier téléchargé dans le répertoire data
mv "human-disease-prediction-dataset.zip" data/
unzip data/human-disease-prediction-dataset.zip
echo "Dossier dézipé"

mv "testing.csv" "training.csv" data/
echo "Bases sauvegardées dans data"

# Accorder des permissions au répertoire data
chmod -R 777 data

