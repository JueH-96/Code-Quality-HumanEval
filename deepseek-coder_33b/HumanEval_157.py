def right_angle_triangle(a, b, c):
    sides = sorted([a,b,c]) # Sorting the lengths for convenience.
    return sides[2]**2 == sides[0]**2 + sides[1]**2  # Using Pythagoras' theorem for right-angled triangle.