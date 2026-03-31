def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has
    total number of chars in all strings of the list less than the other list.

    If the two lists have the same number of chars, return the first list.
    '''
    sum1 = sum(len(s) for s in lst1)
    sum2 = sum(len(s) for s in lst2)

    if sum1 < sum2:
        return lst1
    elif sum1 > sum2:
        return lst2
    else:
        return lst1