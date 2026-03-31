def derivative(xs: list):
    """Return the coefficients of the derivative of a polynomial.

    The polynomial is given by the list `xs`, where the element at index `i`
    represents the coefficient for x**i. The derivative is computed using the
    power rule, resulting in a new list of coefficients.

    Examples
    --------
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # For a constant polynomial (length <= 1), the derivative is zero -> empty list.
    return [coef * idx for idx, coef in enumerate(xs)][1:]