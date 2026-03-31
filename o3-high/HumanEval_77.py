def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.

    Examples:
    iscube(1)  ==> True
    iscube(2)  ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0)  ==> True
    iscube(180)==> False
    '''
    # 0 is a perfect cube (0^3)
    if a == 0:
        return True

    # Work with absolute value for searching, sign doesn't affect cubeness
    n = abs(a)

    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        cube = mid * mid * mid
        if cube == n:
            return True
        if cube < n:
            low = mid + 1
        else:
            high = mid - 1

    return False