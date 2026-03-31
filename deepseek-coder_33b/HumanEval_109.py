def move_one_ball(arr):
    # If the list is empty or has only 1 element, it's already sorted
    if len(arr) < 2: return True
    
    rotate_point = None
    for i in range(len(arr)-1):
        if arr[i] > arr[-1]:
            # Found point of rotation. This means we've gone through an entire cycle, and the array is not sorted
            if rotate_point is not None: return False 
            
            rotate_point = i
            
    # If no rotate_point is found, or the last element isn't greater than the first one, then it can be sorted in one operation
    return rotate_point is not None and arr[-1] <= arr[0]