def make_a_pile(n):
    """
    Given a positive integer n, build a pile of n levels of stones.
    The first level contains n stones. Each subsequent level contains
    the next odd number of stones if n is odd, or the next even number
    if n is even.

    The function returns a list where the element at index i represents
    the number of stones in level (i + 1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    >>> make_a_pile(4)
    [4, 6, 8, 10]
    """
    return [n + 2 * i for i in range(n)]