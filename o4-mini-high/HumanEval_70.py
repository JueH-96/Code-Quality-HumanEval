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
    sorted_list = sorted(lst)
    result = []
    left, right = 0, len(sorted_list) - 1
    take_small = True
    while left <= right:
        if take_small:
            result.append(sorted_list[left])
            left += 1
        else:
            result.append(sorted_list[right])
            right -= 1
        take_small = not take_small
    return result