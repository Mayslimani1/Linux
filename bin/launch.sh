#!/bin/bash

echo "Downloading data"
bash data_collector/run.sh 
echo "Data downloaded" 
echo "Integrating data" 
bash data_integrator/bin/workflow.sh 
echo "Data integrated" 
bash app.sh
echo "Application en cours"