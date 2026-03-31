def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    '''
    counts = {}
    for i in range(len(lst)):
        if i < len(lst) - 1 and lst[i] > lst[i + 1]:
            return False
        counts[lst[i]] = counts.get(lst[i], 0) + 1
        if counts[lst[i]] > 2:
            return False
    return True