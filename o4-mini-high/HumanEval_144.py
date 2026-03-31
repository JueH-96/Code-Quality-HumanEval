def simplify(x, n):
    nx, dx = map(int, x.split('/'))
    nn, dn = map(int, n.split('/'))
    num = nx * nn
    den = dx * dn
    return num % den == 0