def smallest_change(arr):
    i = 0
    j = len(arr) - 1
    count = 0
    while i <= j:
        if arr[i] != arr[j]:
            count += 1
        i += 1
        j -= 1
    
    return (count + 1) // 2