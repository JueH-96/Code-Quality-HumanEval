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
    sign = 1 if a > 0 else -1
    n = abs(a)
    # approximate integer cube root
    root = int(n ** (1/3))
    # check possible candidates
    for k in (root - 1, root, root + 1, root + 2):
        if k >= 0 and (k ** 3) == n:
            return True
    return False