def search(lst):
    from collections import Counter
    
    frequency = Counter(lst)
    result = -1
    
    for num in frequency:
        if num > 0 and frequency[num] >= num:
            result = max(result, num)
    
    return result