import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
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
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")

    # Find the index of the largest non-zero coefficient
    max_coeff_index = [i for i, coeff in enumerate(xs) if abs(coeff) > 0]
    max_coeff_index = max(max_coeff_index)

    # Use Newton's method to find a root
    def derivative(xs: list, x: float):
        return sum([coeff * (len(xs) - i - 1) * math.pow(x, len(xs) - i - 2) for i, coeff in enumerate(xs)])

    def newton_raphson(xs: list, initial_guess: float):
        tolerance = 1e-5
        max_iterations = 1000

        x = initial_guess
        for _ in range(max_iterations):
            if abs(poly(xs, x)) < tolerance:
                return x
            elif derivative(xs, x) == 0:
                raise ValueError("Derivative is zero. Cannot proceed with Newton's method.")
            else:
                x = x - poly(xs, x) / derivative(xs, x)
        return x

    # Start the search from a point that guarantees convergence to a real root
    initial_guess = -xs[0] / xs[max_coeff_index]
    if max_coeff_index % 2 != 0:
        initial_guess *= -1

    return newton_raphson(xs, initial_guess)