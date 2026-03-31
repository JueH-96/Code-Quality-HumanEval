def even_odd_count(num):
    """Given an integer, return a tuple containing the number of even and odd
    digits respectively.

    Examples:
        even_odd_count(-12)  -> (1, 1)
        even_odd_count(123)  -> (1, 2)
    """
    num = abs(num)  # Ignore sign for digit counting
    # Special case: num == 0 has one digit which is even
    if num == 0:
        return (1, 0)
    
    even = odd = 0
    while num:
        digit = num % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return (even, odd)