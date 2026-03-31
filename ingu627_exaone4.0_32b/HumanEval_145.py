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
        n = abs(n)
        return sum(int(d) for d in str(n))
    
    # Create a list of tuples: (digit_sum, original index, value)
    indexed_nums = [(digit_sum(num), idx, num) for idx, num in enumerate(nums)]
    # Sort by digit_sum, then by original index
    indexed_nums.sort(key=lambda x: (x[0], x[1]))
    # Extract the sorted numbers
    sorted_nums = [num for (_, _, num) in indexed_nums]
    return sorted_nums