#!/bin/bash

TRIALNAME0="./data_creation.py"
TRIALNAME1="./data_preprocessing.py"
TRIALNAME2="./model_preparation.py"
TRIALNAME3="./model_testing.py"


sudo chmod +x $TRIALNAME0
sudo chmod +x $TRIALNAME1
sudo chmod +x $TRIALNAME2
sudo chmod +x $TRIALNAME3
sudo chmod +x $TRIALNAME4

python ./data_creation.py
python ./data_preprocessing.py
python ./model_preparation.py
python ./model_testing.py
