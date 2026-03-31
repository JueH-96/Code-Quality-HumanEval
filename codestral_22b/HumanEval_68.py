def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list, [smallest_value, its index],
    If there are no even values or the given array is empty, return [].
    """
    min_val = float('inf')
    min_idx = -1
    for idx, val in enumerate(arr):
        if val % 2 == 0 and val < min_val:
            min_val = val
            min_idx = idx
    return [min_val, min_idx] if min_idx != -1 else []