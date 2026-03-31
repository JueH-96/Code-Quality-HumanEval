def search(lst):
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    result = -1
    for key, value in frequency.items():
        if key <= value and key > result:
            result = key
    return result