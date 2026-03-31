import math

def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    # Special case for zero
    if a == 0:
        return True
    
    # Compute the approximate cube root, preserving the sign of a
    cube_root = math.copysign(abs(a) ** (1/3), a)
    
    # Get the nearest integer to the cube root
    n = int(round(cube_root))
    
    return n ** 3 == a