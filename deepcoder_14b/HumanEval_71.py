import math

def triangle_area(a, b, c):
    # Check if any side is non-positive
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    # Check if the sides satisfy the triangle inequality theorem
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        return -1
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area_sq = s * (s - a) * (s - b) * (s - c)
    if area_sq <= 0:
        return -1  # This condition is theoretically unreachable due to earlier checks
    area = math.sqrt(area_sq)
    return area