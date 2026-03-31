def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    
    # Total n-digit numbers
    total = 9 * (10 ** (n - 1))
    
    # Numbers that start with 1
    starts_with_1 = 10 ** (n - 1)
    
    # Numbers that end with 1
    ends_with_1 = 9 * (10 ** (n - 2))
    
    # Numbers that both start and end with 1
    both = 10 ** (n - 2)
    
    # Using inclusion-exclusion principle
    return starts_with_1 + ends_with_1 - both