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
    if a == 0:
        return True
    # For positive numbers, cube root is straightforward.
    # For negative numbers, cube root of -a is -cube_root(a)
    if a > 0:
        candidate = round(a ** (1/3))
    else:
        candidate = -round((-a) ** (1/3))
    return candidate ** 3 == a