#!/bin/bash

sudo apt install python3-pip
pip install numpy
pip install pandas
pip install -U scikit-learn

TRIALNAME0=`sudo find / -path \*mops_pract-main/lab1/data_creation.py`
TRIALNAME1=`sudo find / -path \*mops_pract-main/lab1/data_preprocessing.py`
TRIALNAME2=`sudo find / -path \*mops_pract-main/lab1/model_preparation.py`
TRIALNAME3=`sudo find / -path \*mops_pract-main/lab1/model_testing.py`


sudo chmod +x $TRIALNAME0
sudo chmod +x $TRIALNAME1
sudo chmod +x $TRIALNAME2
sudo chmod +x $TRIALNAME3

sudo python3 $TRIALNAME0
sudo python3 $TRIALNAME1
sudo python3 $TRIALNAME2
sudo python3 $TRIALNAME3
