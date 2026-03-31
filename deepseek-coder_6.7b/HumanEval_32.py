import math
from typing import List

def poly(xs: List[float], x: float) -> float:
    """Evaluates polynomial with coefficients xs at point x."""
    return sum([coeff * pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: List[float]) -> float:
    """Find the zero of a polynomial. Uses bisection method."""
    assert len(xs) % 2 == 1, "List xs must have odd number of coefficients"
    max_coeff = max(abs(c) for c in xs[:-1])
    left, right = 0.0, 1.0 / (max_coeff + 1)
    while abs(poly(xs, left)) > 1e-6:
        mid = (left + right) / 2
        if poly(xs, mid) * poly(xs, left) <= 0:
            right = mid
        else:
            left = mid
    return left