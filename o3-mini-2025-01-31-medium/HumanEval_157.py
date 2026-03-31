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
    sides = sorted([a, b, c])
    
    # Check if the sides can form a triangle
    if sides[0] + sides[1] <= sides[2]:
        return False
    
    # Check for right-angle using Pythagoras theorem
    return abs(sides[2]**2 - (sides[0]**2 + sides[1]**2)) < 1e-9