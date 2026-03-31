import math

def sum_squares(lst):
    """Return the sum of the squares of the ceiling of each number in lst."""
    return sum(int(math.ceil(x)) ** 2 for x in lst)