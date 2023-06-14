import numpy
from sklearn.linear_model import LogisticRegression
import pickle

X_train = np.loadtxt('x_train.csv', delimiter=',')
y_train = np.loadtxt('y_train.csv', delimiter=',')

model = LogisticRegression()

model.fit(X_train, y_train)

#Saving
pkl_filename = "pickle_model.pkl" 
with open(pkl_filename, 'wb') as file: 
    pickle.dump(model, file)

