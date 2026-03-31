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
    Moreover, find_zero only takes lists xs having an even number of coefficients
    and the largest non-zero coefficient as it guarantees a solution.
    """
    # initial bounds for bisection method
    lower_bound = -100  # assuming polynomial behavior near this point
    upper_bound = 100  # assuming polynomial behavior near this point

    # tolerance for zero finding
    epsilon = 1e-6

    while abs(upper_bound - lower_bound) > epsilon:
        midpoint = (lower_bound + upper_bound) / 2
        if poly(xs, midpoint) * poly(xs, lower_bound) < 0:
            upper_bound = midpoint
        else:
            lower_bound = midpoint
    return midpoint