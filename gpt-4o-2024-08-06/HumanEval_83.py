def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1  # Only the number 1 itself

    # Total n-digit numbers
    total_n_digit_numbers = 9 * (10 ** (n - 1))

    # Numbers starting with 1: 1XX...X (n-1 digits after 1)
    start_with_1 = 10 ** (n - 1)

    # Numbers ending with 1: XX...X1 (n-1 digits before 1)
    end_with_1 = 10 ** (n - 1)

    # Numbers that start and end with 1: 1XX...X1 (n-2 digits between)
    start_and_end_with_1 = 10 ** (n - 2)

    # Total numbers that start or end with 1
    return start_with_1 + end_with_1 - start_and_end_with_1