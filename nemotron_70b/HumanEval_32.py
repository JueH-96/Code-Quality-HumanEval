def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having an even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    """
    # Check for even number of coefficients
    assert len(xs) % 2 == 0, "List must have an even number of coefficients"
    
    # Find the index of the last non-zero coefficient (assumed to be at the end)
    while xs[-1] == 0:
        xs.pop()
        assert len(xs) > 0, "All coefficients are zero"

    # Use Newton-Raphson method for finding a root
    def poly(xs: list, x: float):
        """
        Evaluates polynomial with coefficients xs at point x.
        return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
        """
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

    def derivative(xs: list, x: float):
        """Derivative of the polynomial"""
        return sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs[1:], 1)])

    # Initial guess
    x = -xs[-2] / xs[-1] if len(xs) > 1 else 0

    # Tolerance and max iterations
    tol = 1e-6
    max_iter = 1000

    for _ in range(max_iter):
        f_x = poly(xs, x)
        if abs(f_x) < tol:
            break
        df_x = derivative(xs, x)
        x -= f_x / df_x

    return x