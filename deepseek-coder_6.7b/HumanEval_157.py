def right_angle_triangle(a, b, c):
    # Sort the sides in ascending order
    sides = sorted([a, b, c])

    # The Pythagorean theorem states that in a right-angled triangle, 
    # the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides.
    return sides[0]**2 + sides[1]**2 == sides[2]**2