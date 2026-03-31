def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Create a doubled version of b to account for all rotations
    doubled_b = b + b
    # Check if any rotation of b is a substring of a
    return any(doubled_b[i:i+len(b)] in a for i in range(len(b)))