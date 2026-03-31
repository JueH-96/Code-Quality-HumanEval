def move_one_ball(arr):
    if not arr:
        return True
    
    n = len(arr)
    pivot = 0
    count = 0
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i + 1
            count += 1
    
    if count != 1:
        return False
    
    rotated = arr[pivot:] + arr[:pivot]
    for i in range(len(rotated) - 1):
        if rotated[i] > rotated[i + 1]:
            return False
    
    return True