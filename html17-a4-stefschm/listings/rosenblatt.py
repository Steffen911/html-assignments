def pt_train(X, y, maxepochs=100, w0=None):
    N, D = X.shape
    w = w0 if w0 is None else np.zeros(D)

    yhat = list(map(
        lambda i: i if i == 1 else -1, y))
    ypred = np.sign(X @ w)

    if np.array_equal(ypred, yhat) or \
        maxepochs == 0:
        return w

    for i in range(N):
        if yhat[i] != ypred[i]:
            w += yhat[i] * X[i]

    return pt_train(X, y, maxepochs - 1, w)