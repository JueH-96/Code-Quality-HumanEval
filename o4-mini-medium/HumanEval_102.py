def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.
    """
    high = int(y)
    if high % 2 != 0:
        high -= 1
    if high < x:
        return -1
    return high