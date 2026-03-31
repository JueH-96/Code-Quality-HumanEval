import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
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
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Define the function
    f = lambda x: poly(xs, x)
    # If zero at 0
    if abs(f(0.0)) < 1e-14:
        return 0.0
    # Find bracket [a, b] with sign change
    a, b = -1.0, 1.0
    fa, fb = f(a), f(b)
    step = 1.0
    # Expand until a sign change or limit
    while fa * fb > 0:
        step *= 2
        a, b = -step, step
        fa, fb = f(a), f(b)
        if step > 1e6:
            break
    # Bisection method
    tol = 1e-12
    for _ in range(100):
        m = 0.5 * (a + b)
        fm = f(m)
        if abs(fm) < tol:
            return m
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)