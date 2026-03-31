def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    '''
    if len(lst) <= 1:
        return True

    prev = lst[0]
    count = 1  # occurrences of current number

    for curr in lst[1:]:
        # Check ascending order
        if curr < prev:
            return False

        # Check duplicate count
        if curr == prev:
            count += 1
            if count > 2:
                return False
        else:
            count = 1  # reset count for new number

        prev = curr

    return True