from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(X, y)
yhat = nb.predict(Xtest)

accuracy_score(ytest, yhat)