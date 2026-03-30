def maximum(arr, k):
    sorted_arr = sorted(arr, reverse=True)
    return sorted(sorted_arr[:k])