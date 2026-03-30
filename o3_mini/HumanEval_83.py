def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    # Count numbers starting with 1: 10^(n-1)
    # Count numbers ending with 1: 9 * 10^(n-2) (because the first digit must be 1-9)
    # Count numbers that both start and end with 1: 10^(n-2)
    # Total = 10^(n-1) + 9 * 10^(n-2) - 10^(n-2) = 10^(n-1) + 8*10^(n-2)
    return 10**(n-1) + 8 * 10**(n-2)