def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    max_prime = 1
    # Remove factors of 2
    while n % 2 == 0:
        max_prime = 2
        n //= 2
    # Check odd factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            max_prime = factor
            n //= factor
        factor += 2
    # If remaining n is a prime greater than 2
    if n > 1:
        max_prime = n
    return max_prime