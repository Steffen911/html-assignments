# Compute the priors P(Y)
num = np.bincount(y) + alpha - 1
denom = y.size + K * alpha - K
priors = np.divide(num, denom)