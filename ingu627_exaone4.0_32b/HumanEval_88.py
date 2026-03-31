def sort_array(array):
    if not array:
        return []
    first = array[0]
    last = array[-1]
    total = first + last
    if total % 2 == 1:
        return sorted(array)
    else:
        return sorted(array, reverse=True)