def k_largest(arr, k):
    if not arr or k <= 0:
        return []
    sorted_arr = sorted(arr)
    effective_k = min(k, len(sorted_arr))
    return sorted_arr[-effective_k:]