def x_or_y(n, x, y):
    """Return x if `n` is prime, else return y.
    
    Examples
    --------
    >>> x_or_y(7, 34, 12)
    34
    >>> x_or_y(15, 8, 5)
    5
    """
    # Primes are positive integers greater than 1
    if not isinstance(n, int) or n <= 1:
        return y
    if n == 2:
        return x
    # Even numbers greater than 2 are not prime
    if n % 2 == 0:
        return y

    # Check odd divisors up to sqrt(n)
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return y
    return x