def triangle_area(a, b, c):
    # Check if all sides are positive
    if a <= 0 or b <= 0 or c <= 0:
        return round(-1)
    
    # Check triangle validity: sum of any two sides must be greater than the third
    if (a + b > c) and (a + c > b) and (b + c > a):
        s = (a + b + c) / 2
        area_squared = s * (s - a) * (s - b) * (s - c)
        # Compute the square root to get the area
        area = area_squared ** 0.5
        return round(area, 2)
    else:
        return -1