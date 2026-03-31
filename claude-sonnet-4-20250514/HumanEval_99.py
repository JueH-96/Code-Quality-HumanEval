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
    num = float(value)
    
    # Get the floor and ceiling of the number
    floor_val = int(num) if num >= 0 else int(num) - 1
    ceil_val = floor_val + 1
    
    # Calculate distances to floor and ceiling
    dist_to_floor = abs(num - floor_val)
    dist_to_ceil = abs(num - ceil_val)
    
    # If equidistant, round away from zero
    if dist_to_floor == dist_to_ceil:
        if num >= 0:
            return ceil_val
        else:
            return floor_val
    # Otherwise, return the closer integer
    elif dist_to_floor < dist_to_ceil:
        return floor_val
    else:
        return ceil_val