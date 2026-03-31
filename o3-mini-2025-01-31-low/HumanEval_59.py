def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Remove factors of 2
    largest_factor = 1
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Now n is odd. We can check odd factors.
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2

    # If n is a prime greater than 2, then it is the largest prime factor.
    if n > 1:
        largest_factor = n

    return largest_factor