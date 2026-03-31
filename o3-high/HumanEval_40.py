def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    It returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    # Need at least three elements to form a triple.
    if len(l) < 3:
        return False

    # Sort the list to enable two-pointer technique.
    nums = sorted(l)
    n = len(nums)

    for i in range(n - 2):
        # Early termination: if the current number is > 0, the sum can't be 0
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                return True
            elif total < 0:
                left += 1
            else:
                right -= 1

    return False