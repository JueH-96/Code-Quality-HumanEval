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
    if a >= 0:
        lo, hi = 0, a
    else:
        lo, hi = a, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cube = mid * mid * mid
        if cube == a:
            return True
        if cube < a:
            lo = mid + 1
        else:
            hi = mid - 1
    return False