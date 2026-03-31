def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word."""
    if len(b) > len(a):
        return False
    
    # Double the first string to handle rotation checks
    doubled_a = a + a
    
    # Check all rotations of b
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in doubled_a:
            return True
    
    return False