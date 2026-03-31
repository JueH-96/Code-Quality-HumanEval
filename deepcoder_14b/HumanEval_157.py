def right_angle_triangle(a, b, c):
    # Check if all sides are positive
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Sort the sides to easily access the largest (hypotenuse)
    sides = sorted([a, b, c])
    x, y, z = sides[0], sides[1], sides[2]
    
    # Check if it's a valid triangle
    if x + y <= z:
        return False
    
    # Using a small epsilon for floating point comparison
    epsilon = 1e-9
    if abs(x**2 + y**2 - z**2) < epsilon:
        return True
    else:
        return False