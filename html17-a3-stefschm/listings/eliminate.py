def eliminate(G, vars):
    Gnew = G.copy()
    if not isinstance(vars, list):
        vars = [ vars ]
    if len(vars) == 0:
        return Gnew

    var, *tail = vars
    factors = list(Gnew.factors_for[var])
    phi = functools.reduce(
        lambda x,y: x * y, factors)
    Gnew.add_factor(phi.marginalize(var))
    Gnew.remove_var(var)
    return eliminate(Gnew, tail)