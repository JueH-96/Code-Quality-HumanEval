def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    # Get the largest integer <= y
    y_int = int(y)
    # Adjust to the nearest even integer
    if y_int % 2 != 0:
        y_int -= 1
    # Check if it's within the range
    if y_int < x:
        return -1
    return y_int