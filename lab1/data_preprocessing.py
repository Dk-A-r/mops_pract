# -*- coding: utf-8 -*-
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

scaler = StandardScaler()

#1
df_1_ts = pd.read_csv('test/1.csv')#, header=None)
df_1_tr = pd.read_csv('train/1.csv')#, header=None)

#2
df_2_ts = pd.read_csv('test/2.csv')#, header=None)
df_2_tr = pd.read_csv('train/2.csv')#, header=None)


#Стандартизируем и выводим в csv
std_tr_1 = scaler.fit_transform(df_1_tr[['Время']])
std_ts_1 = scaler.fit_transform(df_1_ts[['Время']])
np.savetxt('train/1_std.csv', std_tr_1, delimiter=',')
np.savetxt('test/1_std.csv', std_ts_1, delimiter=',')

std_tr_2 = scaler.fit_transform(df_2_tr[['Время']])
std_ts_2 = scaler.fit_transform(df_2_ts[['Время']])
np.savetxt('train/2_std.csv', std_tr_2, delimiter=',')
np.savetxt('test/2_std.csv', std_ts_2, delimiter=',')
