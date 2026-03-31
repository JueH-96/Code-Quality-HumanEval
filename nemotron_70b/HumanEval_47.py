def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    7.5
    """
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 1:
        # If the length of the list is odd, return the middle element
        return sorted_l[n // 2]
    else:
        # If the length of the list is even, return the average of two middle elements
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2.0