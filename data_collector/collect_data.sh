#!/bin/bash

source .venv/bin/activate

curl -o data.csv "https://data.cdc.gov/api/views/hfr9-rurv/rows.csv?accessType=DOWNLOAD"
echo "Téléchargement terminé"

mkdir -p data

# Déplacer le fichier CSV dans le répertoire "data"
mv data.csv data/

# Accorder des permissions au répertoire "data"
chmod -R 777 data
