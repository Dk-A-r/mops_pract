from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

scaler = StandardScaler()

#Линейная
df_ts_lin = pd.read_csv('test/lin_true.csv')#, header=None)
df_tr_lin = pd.read_csv('train/lin.csv')#, header=None)

#Полиномиальная
df_ts_pol = pd.read_csv('test/pol_true.csv')#, header=None)
df_tr_pol = pd.read_csv('train/pol.csv')#, header=None)

#Гармоническая
df_ts_sin=pd.read_csv('test/sin_true.csv')#, header=None)
df_tr_sin = pd.read_csv('train/sin.csv')#, header=None)

#Стандартизируем и выводим в csv
lin_tr_std = scaler.fit_transform(df_tr_lin[['Скорость']])
lin_ts_std = scaler.fit_transform(df_ts_lin[['Скорость']])
np.savetxt('train/lin_std.csv', lin_tr_std, delimiter=',')
np.savetxt('test/lin_std.csv', lin_ts_std, delimiter=',')

pol_tr_std = scaler.fit_transform(df_tr_pol[['Время']])
pol_ts_std = scaler.fit_transform(df_ts_pol[['Время']])
np.savetxt('train/pol_std.csv', pol_tr_std, delimiter=',')
np.savetxt('test/pol_std.csv', pol_ts_std, delimiter=',')

sin_tr_std = scaler.fit_transform(df_tr_sin[['Угол']])
sin_ts_std = scaler.fit_transform(df_ts_sin[['Угол']])
np.savetxt('train/sin_std.csv', sin_tr_std, delimiter=',')
np.savetxt('test/sin_std.csv', sin_ts_std, delimiter=',')


