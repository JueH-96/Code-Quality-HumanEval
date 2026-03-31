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
    from math import isclose

    # Sort the sides so that the largest side is last
    sides = sorted((a, b, c))

    # All sides must be positive
    if sides[0] <= 0:
        return False

    # Triangle inequality: sum of two smaller sides must be greater than the largest
    if sides[0] + sides[1] <= sides[2]:
        return False

    # Check Pythagorean theorem with tolerance for floating-point arithmetic
    return isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9, abs_tol=1e-9)