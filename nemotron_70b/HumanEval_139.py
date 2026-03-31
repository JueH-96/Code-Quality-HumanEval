def special_factorial(n):
    """
    The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    def factorial(x):
        """Helper function to calculate traditional factorial"""
        if x == 0 or x == 1:
            return 1
        else:
            return x * factorial(x-1)

    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    
    return result