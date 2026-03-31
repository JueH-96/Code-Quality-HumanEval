def triangle_area(a, h):
    """Given length of a side and height return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    try:
        return (a * h) / 2.0
    except TypeError:
        raise TypeError("Both base and height must be numbers")