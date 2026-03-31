def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    '''
    # Check ascending order (non-decreasing)
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False

    # Check duplicate counts
    from collections import Counter
    counts = Counter(lst)
    for count in counts.values():
        if count > 2:
            return False

    return True