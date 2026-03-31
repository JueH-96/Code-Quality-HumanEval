def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    '''
    # Check if the list is sorted in non-decreasing order.
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    
    # Check for more than one duplicate (i.e., an element appearing more than twice)
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > 2:
            return False
            
    return True