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
    # Make a sorted copy of the input list
    sorted_lst = sorted(lst)
    result = []
    left, right = 0, len(sorted_lst) - 1
    # Toggle flag: True means take from the left (min), False means take from the right (max)
    take_left = True

    while left <= right:
        if take_left:
            result.append(sorted_lst[left])
            left += 1
        else:
            result.append(sorted_lst[right])
            right -= 1
        take_left = not take_left

    return result