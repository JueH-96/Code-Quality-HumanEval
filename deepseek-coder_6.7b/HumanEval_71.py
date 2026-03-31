import math

def triangle_area(a, b, c):
    if (a + b > c) and (b + c > a) and (c + a > b): # check for valid triangle
        s = (a + b + c) / 2   # semi-perimeter
        return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)  # Heron's formula
    else:
        return -1