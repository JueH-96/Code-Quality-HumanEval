def triangle_area(a, h):
    """Return the area of a triangle given its base length `a` and height `h`.
    
    Parameters
    ----------
    a : int or float
        The length of the triangle's base.
    h : int or float
        The height corresponding to the base.
    
    Returns
    -------
    float
        The area of the triangle, calculated as (a * h) / 2.
    
    Examples
    --------
    >>> triangle_area(5, 3)
    7.5
    """
    # Basic validation to ensure inputs are numeric and non-negative
    for name, value in (("a", a), ("h", h)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number, got {type(value).__name__!s}")
        if value < 0:
            raise ValueError(f"{name} must be non-negative, got {value!r}")

    return (a * h) / 2