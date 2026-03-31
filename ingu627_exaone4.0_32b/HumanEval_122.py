def add_elements(arr, k):
    total = 0
    for num in arr[:k]:
        if abs(num) < 100:
            total += num
    return total