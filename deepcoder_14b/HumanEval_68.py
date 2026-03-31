def pluck(arr):
    if not arr:
        return []
    
    min_value = None
    min_index = -1

    for i, num in enumerate(arr):
        if num % 2 == 0:
            if (min_value is None) or (num < min_value):
                min_value = num
                min_index = i
    
    if min_value is not None:
        return [min_value, min_index]
    else:
        return []