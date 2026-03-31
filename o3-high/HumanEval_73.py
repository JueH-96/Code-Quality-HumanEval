def smallest_change(arr):
    """
    Given an array `arr` of integers, return the minimum number of elements
    that must be modified so that the array becomes palindromic.

    A palindromic array reads the same forwards and backwards. For each
    mismatched symmetric pair (arr[i], arr[-i-1]), one element change is
    sufficient to make them equal.

    Examples
    --------
    >>> smallest_change([1, 2, 3, 5, 4, 7, 9, 6])
    4
    >>> smallest_change([1, 2, 3, 4, 3, 2, 2])
    1
    >>> smallest_change([1, 2, 3, 2, 1])
    0
    """
    n = len(arr)
    changes = 0
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            changes += 1
    return changes