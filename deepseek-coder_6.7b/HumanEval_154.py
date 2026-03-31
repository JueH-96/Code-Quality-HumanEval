def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    
    # Check if both strings have equal length
    if len(b) != len(a):
        return False
  
    # Create all possible rotations for string b
    rots = [b[i:] + b[:i] for i in range(len(b))]
    
    # Check each rotation against a
    for r in rots:
        if r in a:
            return True
            
    return False