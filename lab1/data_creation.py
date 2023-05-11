import pandas as pd
import numpy as np

def true_fun(x, a=np.pi, b = 0, f=np.sin): 
    """Генерация произвольной зависимости   
    Входные переменные:
    ===========
    x: массив данных из которых будет генерироваться зависимость
    a: коэффициент на который входные данные будут умножаться
    если а - список, то это коэффициенты в полиномиальной зависимости
    так, а = [1,2,3] позволит сгенерировать зависимость вида 1*x+ 2*x^2 +3*x^3 
    b: коэффициент который будет добавлен к данным (постоянная прибавочка)
    f: функция которая будет применена к зависимости. Можно задать списком. Тогда это будут разные колонки
    """
    x = np.atleast_1d(x)[:] # убеждаемся что данные - одномерный массив
    a = np.atleast_1d(a)
    
    if f is None: f = lambda x:x # если функция не задана (None) то ничего не происходит
    x = np.sum([ai*np.power(x, i+1) for i,ai in enumerate(a)],axis=0) # домнажаем входные данные на коэффициенты (и если надо возводим в степень)

    return f(x+ b)
  
  
def noises(shape , noise_power):
    """Генерация случайного шума   
    Входные переменные:
    ===========
    shape: размерность массива данных
    noise_power: коэффициент ~ сила шума
    """
    return np.random.randn(*shape) *noise_power # библиотека numpy может генерировать случайные числа. 
                                                # в данном случае - нормальное распределение (среднее = 0, стандартное отклонение = 1 )
    
   
def dataset(a, b, f = None,  N = 250, x_max =1, noise_power = 0, random_x = True,  seed = 42):
    """Генерация набора данных   
    Входные переменные:
    ===========
    a: коэффициент на который входные данные будут умножаться
    если а - список, то это коэффициенты в полиномиальной зависимости
    так, а = [1,2,3] позволит сгенерировать зависимость вида 1*x+ 2*x^2 +3*x^3 
    b: коэффициент который будет добавлен к данным (постоянная прибавочка)
    f: функция которая будет применена к зависимости. Можно задать списком. Тогда это будут разные колонки
    N: количество точек данных
    x_max: максимальное значение данных
    noise_power: коэффициент ~ сила шума
    random_x: как будут распределены данные (линейно, или случайно)
    seed: фиксированный сид случайных чисел (для повторяемости)
    """

    np.random.seed(seed) # фиксируем случайный seed
    
    if random_x:# если мы хотим случайно распределить данные
        x = np.sort(np.random.rand(N))*x_max # то x будет N случайных числе из диапазона от 0 до x_max
    else: # иначе
        x = np.linspace(0,x_max,N) # х это равномерно распределенные N чисел из диапазона от 0 до x_max
    
    y_true = np.array([]) # создаем пустой массив который будет "наполнять" зависимостями
    
    for f_ in np.append([], f): # если f - задана списком, то мы учтем все варианты
        y_true=np.append(y_true, true_fun(x, a, b, f_)) # применяем описанную выше функцию true_fun
    
    y_true = y_true.reshape(-1,N).T
    y = y_true + noises(y_true.shape , noise_power) # добавляем шум

    return y, y_true, np.atleast_2d(x).T # возвращаем зашумленные значения зависимостей, зависимости без шума, и массив входных данных
  
#Генерация линейной - зависимости 
lin_y, lin_y_true, x = dataset(a=3,
                    b=7,
                    f=[lambda x: x, lambda k: k**2],
                    N=250,
                    x_max=10,
                    noise_power=3,
                   
                    random_x=True,
                    seed=42
                    )
lin_indexes = list(range(250))
lin_col_names = ['x', 'x**2']
df_lin = pd.DataFrame(data = lin_y, 
              index = lin_indexes, 
              columns = lin_col_names)
df_lin_true = pd.DataFrame(data = lin_y, 
              index = lin_indexes, 
              columns = lin_col_names)

#Генерация гармонической зависимости

sin_y, sin_y_true, x = dataset(a=3,
                b=0.333,
                f=[np.sin, np.cos],
                N=1000,
                x_max=10,
                noise_power=0.1,
                random_x=True,
                seed=42
                )
sin_indexes = list(range(1000))
sin_col_names = ['sin', 'cos']
df_sin = pd.DataFrame(data = sin_y, 
              index = sin_indexes, 
              columns = sin_col_names)
df_sin_true = pd.DataFrame(data = sin_y_true, 
              index = sin_indexes, 
              columns = sin_col_names)


#Генерация полинома второй степени

pol_y, pol_y_true, x = dataset(a=[0.32, 0.75],
                b=7,
                f=[lambda x: x, lambda k: k**2],
                N=250,
                x_max=10,
                noise_power=3,
                random_x=True,
                seed=42
                )
pol_indexes = list(range(250))
pol_col_names = ['x', 'x**2']
df_pol = pd.DataFrame(data = pol_y, 
              index = pol_indexes, 
              columns = pol_col_names)
df_pol_true = pd.DataFrame(data = pol_y_true, 
              index = pol_indexes, 
              columns = pol_col_names)

#Сохраняем в файлы

#Сначала тренировочные
df_lin.to_csv('train/lin.csv', index=False)
df_sin.to_csv('train/sin.csv', index=False)
df_pol.to_csv('train/pol.csv', index=False)

#Потом тестовые
df_lin_true.to_csv('test/lin_true.csv', index=False)
df_sin_true.to_csv('test/lin_true.csv', index=False)
df_pol_true.to_csv('test/lin_true.csv', index=False)
