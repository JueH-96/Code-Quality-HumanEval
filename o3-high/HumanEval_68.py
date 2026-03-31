def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    pluck (select) the node with the smallest even value and return it along with its index.

    The result should be returned as [smallest_even_value, its_index].  
    If there are multiple occurrences of the same smallest even value, return the first one
    (i.e., the one with the smallest index).  
    If there are no even numbers in the array or the array is empty, return [].

    Examples
    --------
    >>> pluck([4, 2, 3])
    [2, 1]
    >>> pluck([1, 2, 3])
    [2, 1]
    >>> pluck([])
    []
    >>> pluck([5, 0, 3, 0, 4, 2])
    [0, 1]
    """
    min_even = None
    min_index = -1

    for idx, value in enumerate(arr):
        if value % 2 == 0:  # even check
            if min_even is None or value < min_even:
                min_even = value
                min_index = idx
            # if value == min_even, we keep the earlier index found first

    return [] if min_even is None else [min_even, min_index]