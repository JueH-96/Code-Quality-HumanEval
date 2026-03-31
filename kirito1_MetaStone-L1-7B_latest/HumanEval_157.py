def right_angle_triangle(a, b, c):
    # Check for positive lengths of all sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Sort the sides to easily identify the hypotenuse
    sides = sorted([a, b, c])
    # Apply Pythagorean theorem
    return (sides[0] ** 2 + sides[1] ** 2) == sides[2] ** 2