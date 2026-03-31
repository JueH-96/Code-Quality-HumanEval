def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Lists with fewer than two elements are trivially monotonic
    if len(l) < 2:
        return True

    increasing = True
    decreasing = True

    for prev, curr in zip(l, l[1:]):
        if curr > prev:
            decreasing = False
        elif curr < prev:
            increasing = False

        # Early exit if neither monotonic condition can hold
        if not increasing and not decreasing:
            return False

    return True