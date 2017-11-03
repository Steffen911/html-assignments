def gibbs(G, vars, log=False):
    for var in vars:
        factors = G.factors_for[var]
        sample = functools.reduce(
            lambda x,y: x * y, factors)
        index = sample.indexOf(var)
        positions = list(map(
            lambda x: x.value, sample.vars))
        perc = []
        for i in range(0, var.K):
            positions[index] = i
            perc.append(sample.values[
                tuple(positions)
            ])
        var.value = np.random.choice(
            range(0, var.K),
            p=(perc / sum(perc))
        )