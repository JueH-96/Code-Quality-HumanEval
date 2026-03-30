def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    '''
    if len(lst) <= 1:
        return True
    
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
        if i > 1 and lst[i] == lst[i - 1] == lst[i - 2]:
            return False
    
    return True