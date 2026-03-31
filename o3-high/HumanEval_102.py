def choose_num(x, y):
    """Return the greatest even integer within the inclusive range [x, y].
    
    If no even integer exists in the range, or if x > y, return -1.
    """
    # Ensure proper ordering of the interval
    if x > y:
        return -1

    # Find the largest even number <= y
    largest_even = y if y % 2 == 0 else y - 1

    # Verify it lies within the lower bound
    return largest_even if largest_even >= x else -1