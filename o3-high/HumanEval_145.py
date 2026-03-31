def order_by_points(nums):
    """
    Sorts a list of integers in ascending order according to the sum of their
    digits. If two numbers have the same digit sum, they retain their original
    order (stable sort).

    Examples
    --------
    >>> order_by_points([1, 11, -1, -11, -12])
    [1, -1, 11, -11, -12]
    >>> order_by_points([])
    []
    """
    def digit_sum(n):
        return sum(int(ch) for ch in str(abs(n)))

    return sorted(nums, key=digit_sum)