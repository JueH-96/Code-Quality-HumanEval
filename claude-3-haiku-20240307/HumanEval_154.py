def cycpattern_check(a, b):
    if b in a:
        return True
    for i in range(1, len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False