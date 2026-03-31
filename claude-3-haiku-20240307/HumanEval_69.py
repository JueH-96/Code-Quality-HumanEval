def search(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    for num, count in freq.items():
        if count >= num:
            return num
    
    return -1