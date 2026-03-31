def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Count of n-digit numbers starting with 1: 1 * 9^(n-1) (since first digit is fixed as 1, and rest can be any of 0-9 excluding leading zeros)
    starts_with_one = 9 ** (n - 1)
    
    # Count of n-digit numbers ending with 1: 9 * 9^(n-2) * 1 (since last digit is fixed as 1, first digit can't be zero, and rest can be any of 0-9)
    if n == 1:
        ends_with_one = 1
    else:
        ends_with_one = 9 * (9 ** (n - 2))
    
    # Subtract overlap where numbers both start and end with 1: 9^(n-2) (since first and last digits are fixed as 1, and rest can be any of 0-9 excluding leading zeros)
    if n == 1:
        overlap = 1
    else:
        overlap = 9 ** (n - 2)
    
    # Return total count using principle of inclusion-exclusion
    return starts_with_one + ends_with_one - overlap