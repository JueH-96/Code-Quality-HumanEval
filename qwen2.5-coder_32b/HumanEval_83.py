def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1  # Only the number 1 itself

    # Count numbers starting with 1: 1XXXX... (n-1 X's)
    start_with_1 = 9 ** (n - 1)

    # Count numbers ending with 1: XXXX...1 (n-1 X's)
    end_with_1 = 9 ** (n - 1)

    # Subtract the overlap where numbers both start and end with 1: 1XXX...1 (n-2 X's)
    both_start_and_end_with_1 = 8 ** (n - 2) if n > 1 else 0

    return start_with_1 + end_with_1 - both_start_and_end_with_1