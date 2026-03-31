def smallest_change(arr):
    changes = 0
    n = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            changes += 1
    return changes