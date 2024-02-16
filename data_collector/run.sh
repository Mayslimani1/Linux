#!/bin/bash

echo "Téléchargement en cours"
bash ./data_collector/collect_data.sh
echo "Téléchargement terminé"
sleep 5

chmod -R 777 data_collector