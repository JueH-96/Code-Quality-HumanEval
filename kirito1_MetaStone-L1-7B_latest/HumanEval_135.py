def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values."""
    if len(arr) < 2:
        return -1
    
    max_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            if i > max_index:
                max_index = i
    return max_index