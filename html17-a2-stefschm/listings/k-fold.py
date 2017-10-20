from sklearn.metrics import accuracy_score

i = 0
alpha = 2
alphas = np.zeros(K)
accurracies = np.zeros(K)

for i_train, i_test in Kf.split(X):
    X_train, X_test = X[i_train], X[i_test]
    y_train, y_test = y[i_train], y[i_test]

    x_model = nb_train(X_train, y_train,
                       alpha=i+alpha)
    x_pred = nb_predict(x_model, X_test)

    accurracies[i] = accuracy_score(
        y_test,
        x_pred['yhat']
    )
    alphas[i] = i + alpha
    i += 1