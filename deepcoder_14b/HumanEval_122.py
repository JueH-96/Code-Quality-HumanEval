def add_elements(arr, k):
    total = 0
    for num in arr[:k]:
        if len(str(abs(num))) <= 2:
            total += num
    return total