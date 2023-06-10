import pandas as pd

#read .csv into DF
data_train = pd.read_csv('data_train.csv')
X_train = data_train[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']].values
y_train = data_train['Survived'].values

#load ML model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=100_000).fit(X_train, y_train)

#save and dump fitted model
import pickle
pickle.dump(model, open('model.pkl', 'wb'))
