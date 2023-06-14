import pandas as pd
import numpy as np
from sklearn import preprocessing as prep
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2

df = pd.read_csv('./cars_moldova.csv', delimiter=',')

df = df.drop_duplicates()
df = df.reset_index(drop=True)

#Delete anomalies

question_dist = df[(df.Year <2021) & (df.Distance < 1100)]
df = df.drop(question_dist.index)

question_dist = df[(df.Distance > 1e6)]
df = df.drop(question_dist.index)

question_engine = df[df["Engine_capacity(cm3)"] < 200]
df = df.drop(question_engine.index)

question_engine = df[df["Engine_capacity(cm3)"] > 5000]
df = df.drop(question_engine.index)

question_price = df[(df["Price(euro)"] < 101)]
df = df.drop(question_price.index)

question_price = df[df["Price(euro)"] > 1e5]
df = df.drop(question_price.index)

question_year = df[df.Year < 1971]
df = df.drop(question_year.index)

df = df.reset_index(drop=True)

#Add OHE

transmission = {'Manual': 1, 'Automatic': 0}
df['Transmission'] = [transmission[item] for item in df['Transmission']]

Y = df['Transmission']

X = df.drop(['Transmission'], axis=1)

num_columns = X.select_dtypes(include=np.number).columns #select only numeric-columns
cat_columns = X.drop(num_columns, axis=1).columns

X_dum = pd.get_dummies(X[cat_columns])

X_new = pd.concat([X[num_columns], X_dum], axis=1)

X_new = X_new.to_numpy()

X_new = SelectKBest(chi2, k=100).fit_transform(X_new, Y) #select best predictors

#divide samples

X_train, X_test, y_train, y_test = train_test_split(
    X_new, Y, test_size=0.33, random_state=42)

#save

np.savetxt('x_train.csv', X_train, delimiter=',')
np.savetxt('x_test.csv', X_test, delimiter=',')
np.savetxt('y_train.csv', y_train, delimiter=',')
np.savetxt('y_test.csv', y_test, delimiter=',')
