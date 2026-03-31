def move_one_ball(arr):
    """Determine whether the given array can be transformed into non-decreasing
    order using any number of right-shift (cyclic rotation) operations."""
    # An empty array or single element is trivially sortable
    n = len(arr)
    if n <= 1:
        return True

    # Count positions where the ascending order is "broken"
    breaks = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:  # compare with next element cyclically
            breaks += 1
            if breaks > 1:             # More than one break means not a rotation of sorted array
                return False
    return True