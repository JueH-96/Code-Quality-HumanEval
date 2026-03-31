def move_one_ball(arr):
    if not arr:
        return True
    
    n = len(arr)
    sorted_arr = sorted(arr)
    
    # Create a string representation of both the original and sorted arrays
    arr_str = ','.join(map(str, arr))
    sorted_str = ','.join(map(str, sorted_arr))
    
    # Check if the sorted array can be obtained by any number of right rotations
    for i in range(n):
        # Rotate the array to the right by i positions
        rotated = arr[-i:] + arr[:-i]
        rotated_str = ','.join(map(str, rotated))
        if rotated_str == sorted_str:
            return True
    
    return False