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
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Use bisection method.
    tol = 1e-7
    max_iter = 1000
    
    # first, choose two values a and b such that f(a)*f(b) < 0.
    a = 0.0
    fa = poly(xs, a)
    # if f(0) is 0, return 0 immediately.
    if abs(fa) < tol:
        return a
    
    # We'll search in both negative and positive directions.
    step = 1.0
    found = False
    # Try to find left bound
    left = a
    right = a
    for _ in range(max_iter):
        left = a - step
        right = a + step
        fleft = poly(xs, left)
        fright = poly(xs, right)
        if fleft * fa < 0:
            a, b = left, 0
            found = True
            break
        if fright * fa < 0:
            a, b = 0, right
            found = True
            break
        if fleft * fright < 0:
            a, b = left, right
            found = True
            break
        step *= 2
    if not found:
        raise ValueError("Failed to bracket the root.")
    
    # Ensure a is the left bound
    if a > b:
        a, b = b, a

    # Bisection iteration.
    for _ in range(max_iter):
        mid = (a + b) / 2.0
        fmid = poly(xs, mid)
        if abs(fmid) < tol or (b - a) / 2 < tol:
            return mid
        if poly(xs, a) * fmid < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2.0