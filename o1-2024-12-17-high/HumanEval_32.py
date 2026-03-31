def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(xs, x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having an even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2)  # (x - 1)*(x - 2)*(x - 3) -> -6 + 11x - 6x^2 + x^3
    1.0
    """
    def f(x):
        import math
        return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))
    
    a, b = -1.0, 1.0
    fa, fb = f(a), f(b)
    # Expand interval until sign change or hitting iteration limit
    for _ in range(200):
        if fa * fb <= 0:
            break
        if abs(fa) < abs(fb):
            a *= 2
            fa = f(a)
        else:
            b *= 2
            fb = f(b)
    
    # Bisection method
    for _ in range(200):
        mid = (a + b) / 2
        fm = f(mid)
        if abs(fm) < 1e-12:
            return mid
        if fa * fm <= 0:
            b = mid
            fb = fm
        else:
            a = mid
            fa = fm
    return (a + b) / 2