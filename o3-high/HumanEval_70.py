def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if not lst:
        return []
    
    sorted_lst = sorted(lst)
    res = []
    left, right = 0, len(sorted_lst) - 1

    while left <= right:
        res.append(sorted_lst[left])
        left += 1
        if left <= right:  # Ensure there is still an element to pick as max
            res.append(sorted_lst[right])
            right -= 1

    return res