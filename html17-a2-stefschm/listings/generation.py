def nb_generate(model, ygen):
    logcls = model['logcls']
    n = len(ygen)
    C,D,K = logcls.shape
    Xgen = np.zeros((n,D))
    for i in range(n):
        c = ygen[i]
        for d in range(D):
            prob = np.exp(logcls[c][d])
            Xgen[i][d] = np.random.choice(
                range(K),
                p=prob
             )
    return Xgen
