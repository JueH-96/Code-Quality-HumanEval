def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Count of n-digit numbers starting with 1
    starts_with_one = 9 * (10 ** (n - 1))
    
    # Count of n-digit numbers ending with 1
    ends_with_one = 9 * (10 ** (n - 1))
    
    # Subtract the count of numbers that start and end with 1 to avoid double counting
    starts_and_ends_with_one = 9 ** (n - 2) if n > 1 else 0
    
    return starts_with_one + ends_with_one - starts_and_ends_with_one