# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

model = LinearRegression(
fit_intercept=True, 
n_jobs=3)

df_tr_1 = pd.read_csv('train/1.csv')
df_tr_2 = pd.read_csv('train/2.csv')
df_tr = pd.concat([df_tr_1, df_tr_2])


Y_train = df_tr['Height'].to_numpy().reshape(-1, 1)
X_train = np.concatenate(
    (np.genfromtxt('train/1_std.csv', delimiter=','),
     np.genfromtxt('train/2_std.csv', delimiter=','))
).reshape(-1, 1)

model.fit(X_train, Y_train)

#Saving
pkl_filename = "pickle_model.pkl" 
with open(pkl_filename, 'wb') as file: 
    pickle.dump(model, file)
