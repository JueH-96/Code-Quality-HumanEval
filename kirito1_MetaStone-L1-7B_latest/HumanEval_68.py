def pluck(arr):
    if not arr:
        return []
    
    min_val = None
    min_index = 0
    
    for i in range(len(arr)):
        val = arr[i]
        if val % 2 == 0:  # Check if the value is even
            if (min_val is None) or (val < min_val):
                min_val = val
                min_index = i
    
    if min_val is not None:
        return [min_val, min_index]
    else:
        return []