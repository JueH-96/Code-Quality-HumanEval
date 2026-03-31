def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1  # Only one number, which is 1 itself
    else:
        starts_with_1 = 10 ** (n - 1)
        ends_with_1 = 9 * 10 ** (n - 2)
        return starts_with_1 + ends_with_1