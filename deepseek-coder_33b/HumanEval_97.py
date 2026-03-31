def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # extract the last digit of both numbers using modulus operator (%)
    a_last = abs(a) % 10
    b_last = abs(b) % 10
    
    # compute product of these two digits and return it
    return a_last * b_last