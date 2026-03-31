import math

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    def f(x):
        return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

    tol = 1e-12
    a, b = -1.0, 1.0
    fa, fb = f(a), f(b)
    if abs(fa) < tol:
        return a
    if abs(fb) < tol:
        return b

    # Expand interval until sign change
    while fa * fb > 0:
        a *= 2.0
        b *= 2.0
        fa, fb = f(a), f(b)

    # Bisection method
    for _ in range(1000):
        m = (a + b) / 2.0
        fm = f(m)
        if abs(fm) < tol or (b - a) / 2 < tol:
            return m
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm

    return (a + b) / 2.0