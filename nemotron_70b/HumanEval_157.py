def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # Sort the sides to ensure a and b are the shorter sides, c is the longest
    a, b, c = sorted([a, b, c])
    
    # Check if the square of the longest side (c) equals the sum of squares of the other two sides
    return a**2 + b**2 == c**2