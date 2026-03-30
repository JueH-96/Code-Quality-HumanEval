def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Count for numbers starting with 1
    start_with_1 = 9 * (10 ** (n - 2)) if n > 1 else 1

    # Count for numbers ending with 1
    end_with_1 = 9 * (10 ** (n - 2)) if n > 1 else 1

    # Subtract the overlap count (numbers that both start and end with 1)
    overlap = 10 ** (n - 2) if n > 1 else 1

    return start_with_1 + end_with_1 - overlap