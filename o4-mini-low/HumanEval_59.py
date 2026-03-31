def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    import math

    max_factor = None

    # Divide out factors of 2
    while n % 2 == 0:
        max_factor = 2
        n //= 2

    # Test odd factors up to sqrt(n)
    factor = 3
    limit = math.isqrt(n) + 1
    while factor <= limit and n > 1:
        while n % factor == 0:
            max_factor = factor
            n //= factor
            limit = math.isqrt(n) + 1
        factor += 2

    # If remaining n is a prime > 2
    if n > 1:
        max_factor = n

    return max_factor