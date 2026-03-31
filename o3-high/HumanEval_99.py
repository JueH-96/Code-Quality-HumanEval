from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING

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
    d = Decimal(value)

    # If it's already an integer, return it directly
    if d == d.to_integral_value():
        return int(d)

    floor_int = int(d.to_integral_value(rounding=ROUND_FLOOR))
    ceil_int = int(d.to_integral_value(rounding=ROUND_CEILING))

    diff_to_floor = d - Decimal(floor_int)
    diff_to_ceil = Decimal(ceil_int) - d

    if diff_to_floor < diff_to_ceil:
        return floor_int
    elif diff_to_ceil < diff_to_floor:
        return ceil_int
    else:  # Equidistant; round away from zero
        return ceil_int if d >= 0 else floor_int