def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        raise ValueError("median() arg is an empty sequence")

    s = sorted(l)
    n = len(s)
    mid = n // 2

    if n % 2:  # odd length
        return s[mid]
    else:      # even length
        # Following the examples: average the element at mid and the next element.
        if n == 2:  # special-case for length 2 to avoid index error
            return (s[0] + s[1]) / 2.0
        return (s[mid] + s[mid + 1]) / 2.0