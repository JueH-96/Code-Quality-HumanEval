def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    # Numbers starting with 1: 1 * 10^(n-1)
    start_with_1 = 10**(n-1)
    # Numbers ending with 1: first digit can be 1..9 (9 choices) and remaining n-2 digits free
    end_with_1 = 9 * 10**(n-2)
    # Numbers both starting and ending with 1: fix first and last, remaining n-2 digits free
    both = 10**(n-2)
    return start_with_1 + end_with_1 - both