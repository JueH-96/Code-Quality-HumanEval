def cycpattern_check(a, b):
    """Return True if the second word or any of its cyclic rotations
    appears as a substring within the first word."""
    n = len(b)
    if n == 0:
        return True  # empty pattern always matches
    if len(a) < n:
        return False
    rotation = b
    for _ in range(n):
        if rotation in a:
            return True
        rotation = rotation[1:] + rotation[0]
    return False