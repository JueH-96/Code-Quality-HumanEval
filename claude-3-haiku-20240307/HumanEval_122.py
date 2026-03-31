def add_elements(arr, k):
    total = 0
    for i in range(min(k, len(arr))):
        if 0 <= arr[i] < 100:
            total += arr[i]
    return total