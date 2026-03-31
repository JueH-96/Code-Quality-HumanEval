def largest_divisor(n: int) -> int:
    """Return the largest proper divisor of n (the biggest number < n that divides n).

    >>> largest_divisor(15)
    5
    >>> largest_divisor(16)
    8
    >>> largest_divisor(17)   # prime
    1
    >>> largest_divisor(2)
    1
    """
    if n <= 1:
        return 1  # convention: return 1 when no proper divisor exists

    # Check divisors in pairs around sqrt(n)
    from math import isqrt

    sqrt_n = isqrt(n)
    for i in range(sqrt_n, 0, -1):
        if n % i == 0:
            larger = n // i
            if larger != n:
                return larger  # the paired divisor is the largest proper divisor
            # If the paired divisor is n itself, fall back to i (will be < n except when n == 1)
            return i
    return 1  # Fallback, happens only for n == 1