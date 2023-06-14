from numpy import genfromtxt
from sklearn.linear_model import LogisticRegression
import pickle

X_train = genfromtxt('x_train.csv', delimiter=',')
y_train = genfromtxt('y_train.csv', delimiter=',')

model = LogisticRegression()

model.fit(X_train, y_train)

#Saving
pkl_filename = "pickle_model.pkl" 
with open(pkl_filename, 'wb') as file: 
    pickle.dump(model, file)

