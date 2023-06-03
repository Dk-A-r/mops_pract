#!/bin/bash

TRIALNAME0="./mops_pract-main/lab1/data_creation.py"
TRIALNAME1="./mops_pract-main/lab1/data_preprocessing.py"
TRIALNAME2="./mops_pract-main/lab1/model_preparation.py"
TRIALNAME3="./mops_pract-main/lab1/model_testing.py"


sudo chmod +x $TRIALNAME0
sudo chmod +x $TRIALNAME1
sudo chmod +x $TRIALNAME2
sudo chmod +x $TRIALNAME3

python $TRIALNAME0
python $TRIALNAME1
python $TRIALNAME2
python $TRIALNAME3
