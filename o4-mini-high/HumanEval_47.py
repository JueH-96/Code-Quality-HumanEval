def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        raise ValueError("median requires at least one data point")
    l_sorted = sorted(l)
    n = len(l_sorted)
    mid = n // 2
    if n % 2:
        return l_sorted[mid]
    return (l_sorted[mid - 1] + l_sorted[mid]) / 2