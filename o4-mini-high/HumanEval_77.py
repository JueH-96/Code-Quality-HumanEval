def iscube(a):
    """
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    """
    n = abs(a)
    lo, hi = 0, int(n ** (1/3)) + 2
    while lo <= hi:
        mid = (lo + hi) // 2
        cube = mid * mid * mid
        if cube == n:
            return True
        elif cube < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return False