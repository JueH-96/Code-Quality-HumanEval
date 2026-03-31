def maximum(arr, k):
    arr = sorted(arr, reverse=True)
    return arr[:k]