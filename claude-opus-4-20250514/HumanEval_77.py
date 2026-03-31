def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
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
    
    abs_a = abs(a)
    cube_root = round(abs_a ** (1/3))
    
    # Check if cube_root^3 equals abs_a
    if cube_root ** 3 == abs_a:
        return True
    
    # Due to floating point precision, also check cube_root ± 1
    if (cube_root - 1) ** 3 == abs_a:
        return True
    if (cube_root + 1) ** 3 == abs_a:
        return True
    
    return False