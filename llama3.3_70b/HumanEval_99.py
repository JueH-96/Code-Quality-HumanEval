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
    if num % 1 == 0:
        return int(num)
    elif (num + 0.5) % 2 == 0:
        return round(num)
    else:
        if num > 0:
            return math.floor(num) if math.ceil(num) - num < num - math.floor(num) else math.ceil(num)
        else:
            return math.ceil(num) if math.floor(num) - num < num - math.ceil(num) else math.floor(num)

import math