def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    result = []
    lst_copy = sorted(lst)
    
    while lst_copy:
        if len(result) % 2 == 0:
            result.append(lst_copy.pop(0))  # append min
        else:
            result.append(lst_copy.pop(-1))  # append max
    
    return result