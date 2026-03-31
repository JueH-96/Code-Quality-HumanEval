import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x -6x^2 + x^3
    1.0
    """
    def f(x):
        return poly(xs, x)
    
    # if f(0) is exactly zero, return 0 immediately
    if f(0) == 0:
        return 0.0

    # Initialize bounds
    lower, upper = -1.0, 1.0

    # Expand the interval until we bracket a sign change.
    # We assume that the polynomial is odd-degree (since the number of coefficients is even)
    # so it will have opposite signs at extreme ends.
    while f(lower) * f(upper) > 0:
        lower *= 2
        upper *= 2

    # Bisection method parameters
    tol = 1e-7
    while abs(upper - lower) > tol:
        mid = (lower + upper) / 2.0
        f_mid = f(mid)
        if f_mid == 0:
            return mid
        # Decide which subinterval to pick
        if f(lower) * f_mid < 0:
            upper = mid
        else:
            lower = mid
    return (lower + upper) / 2.0