import math

def sum_squares(lst):
    total = 0
    for num in lst:
        rounded = math.ceil(num)
        squared = rounded ** 2
        total += squared
    return total