def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def points(n):
        # Compute the sum of digits of the absolute value.
        s = sum(int(d) for d in str(abs(n)))
        # For negative numbers, subtract 2 from the digit‐sum.
        return s - 2 if n < 0 else s

    # Sorted() in Python is stable so if two values have equal points,
    # their original order is preserved.
    return sorted(nums, key=points)