import math

def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    # Sides must be positive numbers
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    
    # Check the triangle inequality theorem
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    
    # Heron's formula to calculate the area of a triangle
    s = (a + b + c) / 2.0
    area_squared = s * (s - a) * (s - b) * (s - c)
    
    # Numerical stability: protect against small negative due to floating error
    if area_squared < 0:
        area_squared = 0.0
    
    area = math.sqrt(area_squared)
    
    # Round the area to 2 decimal places
    return round(area, 2)