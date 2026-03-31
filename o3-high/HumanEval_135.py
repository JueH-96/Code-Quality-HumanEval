def can_arrange(arr):
    """Return the largest index i such that arr[i] is less than the element
    immediately preceding it (arr[i-1]). If no such index exists, return -1.

    Examples:
        can_arrange([1, 2, 4, 3, 5]) -> 3
        can_arrange([1, 2, 3])       -> -1
    """
    # Start from the end to find the largest (rightmost) index first.
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return i
    return -1