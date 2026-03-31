def smallest_change(arr):
    n = len(arr)
    changes = [0] * n
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            changes[i] = 1
            changes[n - i - 1] = 1
    return sum(changes)