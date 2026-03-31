def cycpattern_check(a, b):
    n = len(b)
    for k in range(n):
        rotated = b[k:] + b[:k]
        if rotated in a:
            return True
    return False