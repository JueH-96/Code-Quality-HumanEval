import math

def is_prime(n):
    """Return True if a given number is prime, and False otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # Primes are integers greater than 1
    if n <= 1 or not isinstance(n, int):
        return False
    # 2 and 3 are primes
    if n <= 3:
        return True
    # Eliminate even numbers and multiples of 3 quickly
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Test potential factors of the form 6k ± 1 up to sqrt(n)
    limit = int(math.isqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True