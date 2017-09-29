# Returns vector of pred. confidence [0,1]
def predict(Xtest, w):
    return sigma(Xtest @ w)

# Returns vector of predictions {0,1}
def classify(X, w):
    def pred(x):
        return 1 if x > 0.5 else 0
    return np.vectorize(pred)(predict(X, w))