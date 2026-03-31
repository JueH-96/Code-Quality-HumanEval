def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    # Validate that all inputs are integers (exclude booleans which are subclasses of int)
    if any(not isinstance(n, int) or isinstance(n, bool) for n in (x, y, z)):
        return False
    
    # Check if any one number equals the sum of the other two
    return x == y + z or y == x + z or z == x + y