# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split


x_1 = np.random.randn(250)*10
x_2 = np.random.randn(250)*20


y_1 = 2000 - x_1**2*10/2  

y_2 = 2000 - x_2**2*10/2


X_1_train, X_1_test, y_1_train, y_1_test = train_test_split(
              x_1, y_1, test_size=0.33, random_state=42)

X_2_train, X_2_test, y_2_train, y_2_test = train_test_split(
              x_2, y_2, test_size=0.33, random_state=42)


#training
df_1_tr = pd.DataFrame({
                        'Time': X_1_train,\
                        'Height': y_1_train
                         })
df_2_tr = pd.DataFrame({
                        'Time': X_2_train,
                        'Height': y_2_train
                         })


#testing
df_1_ts = pd.DataFrame({
                        'Time': X_1_test,\
                        'Height': y_1_test
                         })
df_2_ts = pd.DataFrame({
                        'Time': X_2_test,
                        'Height': y_2_test
                         })


#Check the directory for data

def creatdir(*paths):
    for i in paths:
        isExists = os.path.exists(i)
        if not isExists:
            os.makedirs(i)
            
creatdir('train', 'test')


#Save

#Training first
df_1_tr.to_csv('train/1.csv', index=False)
df_2_tr.to_csv('train/2.csv', index=False)

#Testing second
df_1_ts.to_csv('test/1.csv', index=False)
df_2_ts.to_csv('test/2.csv', index=False)
