#!/bin/bash

sudo mkdir 'train'
sudo mkdir 'test'

TRIALNAME0="data_creation.py"
TRIALNAME1="data_preprocessing.py"
TRIALNAME2="model_preparation.py"
TRIALNAME3="model_testing.py"


sudo chmod a+rwx $TRIALNAME0
sudo chmod a+rwx $TRIALNAME1
sudo chmod a+rwx $TRIALNAME2
sudo chmod a+rwx $TRIALNAME3
sudo chmod a+rwx $TRIALNAME4

python data_creation.py
python data_preprocessing.py
python model_preparation.py
python model_testing.py
