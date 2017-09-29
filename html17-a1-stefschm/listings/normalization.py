from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(X)

# save mean and variance for later use
mean = scaler.mean_
var = scaler.var_

Xz = scaler.transform(X)
Xtestz = scaler.transform(Xtest)