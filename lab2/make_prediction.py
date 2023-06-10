import pickle
import pandas as pd

loaded_model = pickle.load(open('model.pkl', 'rb'))

#read csv into DF
data_test = pd.read_csv('data_test.csv')
X_test = data_test[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']].values

#predict on test sample
print(loaded_model.predict(X_test[0:1]))
