def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    
    # Count of n-digit numbers that start with 1
    starts_with_1 = 10 ** (n - 1)
    
    # Count of n-digit numbers that end with 1
    ends_with_1 = 9 * (10 ** (n - 2))
    
    # Count of n-digit numbers that both start and end with 1
    both_start_and_end_with_1 = 10 ** (n - 2)
    
    # Using inclusion-exclusion principle
    return starts_with_1 + ends_with_1 - both_start_and_end_with_1