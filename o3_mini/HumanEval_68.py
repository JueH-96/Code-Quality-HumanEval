def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes.
    Your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smallest_value, its index ],
    If there are no even values or the given array is empty, return [].
    """
    candidate = None
    candidate_index = -1
    for index, value in enumerate(arr):
        if value % 2 == 0:
            if candidate is None or value < candidate:
                candidate = value
                candidate_index = index
    return [candidate, candidate_index] if candidate is not None else []