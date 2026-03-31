def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start by dividing n by the smallest prime number
    factor = 2
    while n % factor == 0:
        n //= factor
    # Check for next possible factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 2
    # If n is still greater than 1, then it is prime and the largest factor
    if n > 1:
        return n
    return factor