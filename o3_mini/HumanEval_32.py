import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Ensure the polynomial has an odd degree (even number of coefficients)
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even length for an odd degree polynomial.")
    
    # Bisection method
    tol = 1e-12
    max_iter = 1000

    # We need to find an interval [lo, hi] such that poly(lo)*poly(hi) < 0.
    # For an odd degree polynomial, the sign will change from -infinity to +infinity.
    lo, hi = -1.0, 1.0
    f_lo, f_hi = poly(xs, lo), poly(xs, hi)
    
    # Expand the interval until a sign change is found.
    iter_expand = 0
    while f_lo * f_hi > 0 and iter_expand < max_iter:
        lo *= 2
        hi *= 2
        f_lo, f_hi = poly(xs, lo), poly(xs, hi)
        iter_expand += 1
        
    if f_lo == 0:
        return lo
    if f_hi == 0:
        return hi
    
    # Bisection loop
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        f_mid = poly(xs, mid)
        if abs(f_mid) < tol:
            return mid
        if f_lo * f_mid < 0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid

    return (lo + hi) / 2.0