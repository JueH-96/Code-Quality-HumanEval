from typing import List
import math

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
    # factor out 2s
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # factor out odd numbers
    limit = int(math.isqrt(n)) + 1
    i = 3
    while i <= limit and n > 1:
        while n % i == 0:
            factors.append(i)
            n //= i
            limit = int(math.isqrt(n)) + 1
        i += 2
    # if remaining n is prime
    if n > 1:
        factors.append(n)
    return factors