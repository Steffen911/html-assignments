cls += (alpha - 1)
for i in range(C):
    indizes = np.where(y == i)
    for index in indizes[0]:
        for d in range(D):
            cls[i][d][X[index][d]] += 1

    for d in range(D):
        cls[i][d] = np.divide(
            cls[i][d],
            np.sum(cls[i][d])
        )