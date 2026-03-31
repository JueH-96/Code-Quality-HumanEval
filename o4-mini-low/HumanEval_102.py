import math

def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # If the range is invalid
    if x > y:
        return -1

    # Determine the integer bounds within [x, y]
    low = math.ceil(x)
    high = math.floor(y)

    # If there's no integer in the range
    if high < low:
        return -1

    # Find the largest even integer ≤ high
    if high % 2 != 0:
        high -= 1

    # Check if the found even integer is within the valid range
    if high >= low and high % 2 == 0:
        return high
    else:
        return -1