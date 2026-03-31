def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    If no such value exists, return -1.
    '''
    from collections import Counter
    
    freq = Counter(lst)
    candidates = [num for num, count in freq.items() if count >= num]
    
    return max(candidates) if candidates else -1