def sort_array(array):
    if not array:
        return []

    total = array[0] + array[-1]
    sorted_array = sorted(array)

    if total % 2 == 0: # even sum, descending order
        return sorted_array[::-1]
    
    return sorted_array