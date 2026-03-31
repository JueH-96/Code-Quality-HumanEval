def move_one_ball(arr):
    if not arr or len(arr) == 1:
        return True

    min_val = min(arr)
    min_idx = arr.index(min_val)

    for i in range(len(arr)):
        if arr[(i + min_idx) % len(arr)] != i + 1:
            return False

    return True