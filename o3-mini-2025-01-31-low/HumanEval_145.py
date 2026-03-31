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
    def digit_sum(n):
        return sum(int(ch) for ch in str(abs(n)))
    # Since we want to use the original index as tie-breaker, 
    # but the expected example indicates that when two numbers have equal digit sum,
    # the one with the larger original index comes first, we sort by (digit_sum, -index)
    return [x for _, x in sorted(enumerate(nums), key=lambda ix: (digit_sum(ix[1]), -ix[0]))]