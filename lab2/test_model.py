import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

loaded_model = pickle.load(open('pickle_model.pkl', 'rb'))

#read csv
X_test = np.loadtxt('x_test.csv', delimiter=',')
y_test = np.loadtxt('y_test.csv', delimiter=',')

#test model
print('The model score is: ', loaded_model.score(X_test, y_test))
