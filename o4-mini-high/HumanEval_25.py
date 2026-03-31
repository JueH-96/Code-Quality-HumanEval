def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors: List[int] = []
    if n <= 1:
        return factors
    # extract factors of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # extract odd factors
    p = 3
    max_factor = int(n**0.5) + 1
    while p <= max_factor and n > 1:
        while n % p == 0:
            factors.append(p)
            n //= p
            max_factor = int(n**0.5) + 1
        p += 2
    # if remainder is prime
    if n > 1:
        factors.append(n)
    return factors