import numpy as np
def poly_derivative(xs: list, x: float):
    """
    Returns the derivative of a polynomial given its coefficients and point.
    The derivative is calculated using central difference, which is more accurate than forward or backward difference at `x`.
    """
    h = 1e-5  # choose a small increment
    return (poly(xs, x + h) - poly(xs, x - h)) / (2 * h)