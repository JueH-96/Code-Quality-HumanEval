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
    from decimal import Decimal
    d = Decimal(value)
    sign = 1 if d >= 0 else -1
    ad = d.copy_abs()
    floor_val = int(ad)
    diff = ad - floor_val
    if diff < Decimal('0.5'):
        result = floor_val
    else:
        result = floor_val + 1
    return sign * result