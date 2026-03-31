def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    It returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    if not l or len(l) < 2:
        return False

    # Quick check for two zeros
    zero_count = 0
    for num in l:
        if num == 0:
            zero_count += 1
            if zero_count == 2:
                return True

    nums_set = set(l)
    for num in nums_set:
        if num != 0 and -num in nums_set:
            return True

    return False