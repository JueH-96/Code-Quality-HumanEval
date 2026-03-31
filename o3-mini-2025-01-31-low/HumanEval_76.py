def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int = x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    # Special case: 1 is n**0 for any n (except n = 0, but as per examples, n should be >= 1)
    if x == 1:
        return True
    # If n is 1 but x is not 1, no power of 1 will equal x.
    if n == 1:
        return False
    # Continue dividing x by n as long as it's divisible
    while x > 1:
        if x % n != 0:
            return False
        x //= n
    return x == 1