def sort_array(array):
    if not array:
        return []
    sum_val = array[0] + array[-1]
    if sum_val % 2 == 1:
        return sorted(array)
    else:
        return sorted(array, reverse=True)