def iscube(a):
    if a == 0:
        return True
    
    sign = -1 if a < 0 else 1
    abs_a = abs(a)
    
    low = 0
    high = abs_a  # Maximum possible value for n^3

    while low <= high:
        mid = (low + high) // 2
        cube = mid ** 3
        
        if cube == abs_a:
            return True
        elif cube < abs_a:
            low = mid + 1
        else:
            high = mid - 1
            
    # If no exact match found during binary search, check around the last mid value in case of rounding issues
    candidates = [high] if high != low else []
    for candidate in candidates:
        cube_candidate = candidate ** 3
        if abs(cube_candidate) == a:
            return True
    
    return False