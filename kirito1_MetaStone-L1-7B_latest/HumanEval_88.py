def sort_array(array):
    sorted_copy = list(array)  # Create a copy to avoid modifying the original
    n = len(sorted_copy)
    if n <= 1:
        return sorted_copy
    first = sorted_copy[0]
    last = sorted_copy[-1]
    sum_ab = first + last
    if sum_ab % 2 == 1:
        sorted_copy.sort()
    else:
        sorted_copy.sort(reverse=True)
    return sorted_copy