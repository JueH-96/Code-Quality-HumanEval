def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    
    total_count = 9 * (10 ** (n - 1))  # Total n-digit numbers
    start_with_1 = 10 ** (n - 1)       # Numbers starting with 1
    end_with_1 = 10 ** (n - 1)         # Numbers ending with 1
    start_end_with_1 = 1               # Only the number 1...1 (n times) counts for both

    return (start_with_1 + end_with_1 - start_end_with_1)