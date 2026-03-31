def is_sorted(lst):
    if len(lst) <= 1:
        return True
    
    prev = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < prev or lst[i] == prev:
            return False
        prev = lst[i]
    
    return True