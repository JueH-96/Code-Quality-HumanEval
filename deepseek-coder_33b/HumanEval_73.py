def smallest_change(arr):
    temp = arr[::-1]  # reversed copy of original array
    changes = 0      # counter for changes needed

    i, j = 0, len(temp) - 1
    while i < j:
        if arr[i] != temp[j]:
            # replace values in temp from end to start until it matches
            while (arr[i] != temp[j]) and (j > i):
                j -= 1
            
            # increment change counter
            changes += 1
        i += 1
        j -= 1
    return changes