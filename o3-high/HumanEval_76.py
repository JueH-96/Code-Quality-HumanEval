def is_simple_power(x, n):
    """Return True if x is an integer power of n (n ** k == x for some
    non-negative integer k), False otherwise."""
    # Exponent 0 case
    if x == 1:
        return n != 0

    # Handle small special bases
    if n == 0:
        # 0**k = 0 for any positive k
        return x == 0
    if n == 1:
        return x == 1
    if n == -1:
        return x in (1, -1)

    # Positive base greater than 1
    if n > 1:
        if x <= 0:
            return False
        while x % n == 0:
            x //= n
        return x == 1

    # Negative base less than -1
    while abs(x) > 1:
        if x % n != 0:
            return False
        x //= n
    return abs(x) == 1