def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    import math
    x = float(value)
    floor_x = math.floor(x)
    ceil_x = math.ceil(x)
    d_floor = abs(x - floor_x)
    d_ceil = abs(x - ceil_x)
    if d_floor < d_ceil:
        return floor_x
    elif d_floor > d_ceil:
        return ceil_x
    else:
        if x > 0:
            return ceil_x
        else:
            return floor_x