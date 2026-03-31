def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if x < n:  # If x is smaller than n, it can't be a simple power of n.
        return False
    while x % n == 0:  # Divide x by n until x is not divisible by n.
        x /= n
    return x == 1  # If x became 1 after the division, then it's a simple power of n.