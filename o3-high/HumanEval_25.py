from typing import List
import math


def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in ascending order.

    Each prime factor appears as many times as its multiplicity in the factorization.
    The product of all returned factors equals the absolute value of the input.
    For a negative input, -1 is included as the first factor.

    Examples
    --------
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n == 0:
        raise ValueError("Cannot factorize zero.")

    factors: List[int] = []

    # Handle negative numbers
    if n < 0:
        factors.append(-1)
        n = -n

    # Factor out powers of two first
    while n % 2 == 0 and n > 1:
        factors.append(2)
        n //= 2

    # Factor out odd numbers from 3 upward
    i = 3
    max_factor = int(math.isqrt(n)) + 1
    while i <= max_factor and n > 1:
        while n % i == 0:
            factors.append(i)
            n //= i
            max_factor = int(math.isqrt(n)) + 1
        i += 2  # Only test odd numbers

    # If remaining n is greater than 1, it is a prime
    if n > 1:
        factors.append(n)

    return factors