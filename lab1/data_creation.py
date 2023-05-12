import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split

x_lin = np.random.randn(250)*10
x_pol = np.random.randn(250)
x_sin = np.random.randn(1000)

y_lin = x_lin*8 + 7 #значение пути при постоянной скорости x_lin
                    #за время 8 при старте в точке 7

y_pol = 2000 - x_pol**2*10/2  #приближенная высота, на которой находится тело
                              #при свободном падении с высоты 2000 м через
                              #x_pol секунд

y_sin =  ((10*np.cos(x_sin)*10)**2 \
         + (10*np.sin(x_sin) - 10*10)**2)**0.5 #примерная скорость полета при параболическом движении
                                                #под углом x_sin радиан с начальной скоростью 10 после 10 секунд


X_lin_train, X_lin_test, y_lin_train, y_lin_test = train_test_split(
              x_lin, y_lin, test_size=0.33, random_state=42)

X_pol_train, X_pol_test, y_pol_train, y_pol_test = train_test_split(
              x_pol, y_pol, test_size=0.33, random_state=42)

X_sin_train, X_sin_test, y_sin_train, y_sin_test = train_test_split(
              x_sin, y_sin, test_size=0.33, random_state=42)

#Тренировочные данные
df_tr_lin = pd.DataFrame({
                        'Скорость': X_lin_train,\
                        'Путь': y_lin_train
                         })
df_tr_pol = pd.DataFrame({
                        'Время': X_pol_train,
                        'Высота': y_pol_train
                         })
df_tr_sin = pd.DataFrame({
                        'Угол': X_sin_train,
                        'Скорость': y_sin_train
                         })

#Тестовые данные
df_ts_lin = pd.DataFrame({'Скорость': X_lin_test,
                        'Путь': y_lin_test})
df_ts_pol = pd.DataFrame({'Время': X_pol_test,
                        'Высота': y_pol_test})
df_ts_sin = pd.DataFrame({'Угол': X_sin_test,
                        'Скорость': y_sin_test})

#Проверить, есть ли директория для тестовых и тренировочных, если нет, то создать

def creatdir(*paths):
    for i in paths:
        isExists = os.path.exists(i)
        if not isExists:
            os.makedirs(i)
            
creatdir('train', 'test')


#Сохраняем в файлы

#Сначала тренировочные
df_tr_lin.to_csv('train/lin.csv', index=False)
df_tr_sin.to_csv('train/sin.csv', index=False)
df_tr_pol.to_csv('train/pol.csv', index=False)

#Потом тестовые
df_ts_lin.to_csv('test/lin_true.csv', index=False)
df_ts_sin.to_csv('test/sin_true.csv', index=False)
df_ts_pol.to_csv('test/pol_true.csv', index=False)
