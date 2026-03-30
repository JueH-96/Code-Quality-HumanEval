def find_zero(xs: list):
    import scipy.optimize

    def polynomial(x):
        return poly(xs, x)

    # Use the fsolve function from scipy to find a root of the polynomial
    zero, = scipy.optimize.fsolve(polynomial, 0)
    return zero