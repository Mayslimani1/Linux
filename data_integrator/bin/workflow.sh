#!/bin/bash

FILE=data/Grab_SG_Restaurants.csv

if test -f "$FILE"; then
  echo "$FILE exists. Launching integration"
  bash data_integrator/bin/run.sh
  echo "Data integration succeeded"
else
  echo "No raw file detected"
fi