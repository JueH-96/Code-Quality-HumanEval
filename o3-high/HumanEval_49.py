def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    if p == 0:
        raise ValueError("Modulus p must be non-zero.")
    if n < 0:
        # Compute modular inverse of 2 and then exponentiate
        # Uses extended Euclidean algorithm for generality
        def egcd(a, b):
            if b == 0:
                return a, 1, 0
            g, x1, y1 = egcd(b, a % b)
            return g, y1, x1 - (a // b) * y1

        g, x, _ = egcd(2 % p, p)
        if g != 1:
            raise ValueError("2 and p are not coprime; negative exponent undefined.")
        inv2 = x % p
        return pow(inv2, -n, p)
    return pow(2, n, p)