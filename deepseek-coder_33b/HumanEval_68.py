def pluck(arr):
    min_val = float('inf')
    index = -1
    for i, val in enumerate(arr):
        if val % 2 == 0 and val < min_val:
            min_val = val
            index = i
    
    return [] if index == -1 else [min_val, index]