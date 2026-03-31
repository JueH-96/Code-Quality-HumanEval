import math
def iscube(a):
    return math.isclose(round(a ** (1. / 3)) ** 3, a)