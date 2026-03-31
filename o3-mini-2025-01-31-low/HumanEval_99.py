import math

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
    number = float(value)
    lower = math.floor(number)
    upper = math.ceil(number)
    
    diff_lower = number - lower
    diff_upper = upper - number
    
    if diff_lower < diff_upper:
        return lower
    elif diff_lower > diff_upper:
        return upper
    else:
        # equidistant: round away from zero
        return upper if number >= 0 else lower