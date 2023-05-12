import pickle
import sklearn


pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'rb') as file: 
    pickle_model = pickle.load(file)

df_ts_1 = pd.read_csv('test/1.csv')
df_ts_2 = pd.read_csv('test/2.csv')
df_ts = pd.concat([df_ts_1, df_ts_2])

Y_test = df_ts['Высота'].to_numpy().reshape(-1, 1)
X_test = np.concatenate(
    (np.genfromtxt('test/1_std.csv', delimiter=','),
     np.genfromtxt('test/2_std.csv', delimiter=','))
).reshape(-1, 1)

score = pickle_model.score(X_test, Y_test) 
print("Test score: {0:.2f} %".format(100 * score)) 
Ypredict = pickle_model.predict(X_test)
