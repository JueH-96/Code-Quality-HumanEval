def pluck(arr):
    smallest_value = None
    smallest_index = None
    
    for i, val in enumerate(arr):
        if val % 2 == 0:
            if smallest_value is None or val < smallest_value:
                smallest_value = val
                smallest_index = i
                
    return [] if smallest_value is None else [smallest_value, smallest_index]