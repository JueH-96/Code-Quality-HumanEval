import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... + xs[n] * x^n
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    def f(x):
        return poly(xs, x)
    
    # Initial bracket for the root
    a, b = -1.0, 1.0
    while f(a) * f(b) > 0:
        a *= 2.0
        b *= 2.0

    # Bisection method parameters
    tol = 1e-10
    max_iter = 1000

    for _ in range(max_iter):
        mid = (a + b) / 2.0
        f_mid = f(mid)
        if abs(f_mid) < tol:
            return mid
        if f(a) * f_mid < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2.0