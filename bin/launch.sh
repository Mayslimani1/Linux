#!/bin/bash

cp config.toml ~/.streamlit/

echo "Downloading data"
bash data_collector/run.sh 
echo "Data downloaded" 
sleep 5
echo "Integrating data" 
bash data_integrator/bin/run.sh
echo "Data integrated" 
sleep 5
bash webapp/bin/launch.sh
echo "Application en cours"