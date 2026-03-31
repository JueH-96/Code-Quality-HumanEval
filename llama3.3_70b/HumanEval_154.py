def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    def rotate(word):
        return word[1:] + word[0]
    
    for _ in range(len(b)):
        if b in a:
            return True
        b = rotate(b)
        
    return False

# Alternatively, you can also solve this problem using Python's slicing feature and string concatenation.

def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

# Or, more concisely:

def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    return any(b[i:] + b[:i] in a for i in range(len(b)))