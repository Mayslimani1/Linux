#!/bash

cp config.toml ~/.streamlit/

echo "Downloading data"
bash data_collector/collect_data.sh 
echo "Data downloaded" 
sleep 5
echo "Integrating data" 
bash data_integrator/bin/run.sh
echo "Data integrated" 
sleep 5
python3 -m streamlit run app.py --server.port 8950
echo "Application fermée"
 
chmod +x launch.sh