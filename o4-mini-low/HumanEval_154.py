def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    # If b is longer than a, no rotation of b can fit inside a
    if len(b) > len(a):
        return False
    # An empty b is trivially a substring of a
    if not b:
        return True
    # Concatenate b to itself to capture all rotations
    doubled = b + b
    n = len(b)
    # Check each rotation substring of length n
    for i in range(n):
        rotation = doubled[i:i+n]
        if rotation in a:
            return True
    return False