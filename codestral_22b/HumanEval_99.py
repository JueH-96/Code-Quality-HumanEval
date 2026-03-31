def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.
    '''
    num = float(value)
    if num >= 0:
        if num - int(num) < 0.5 or num == int(num):
            return int(num)
        else:
            return int(num) + 1
    else:
        if abs(num) - abs(int(num)) < 0.5 or abs(num) == abs(int(num)):
            return int(num)
        elif num > 0:
            return int(num) + 1
        else:
            return int(num) - 1