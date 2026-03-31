def strange_sort(lst):
    sorted_lst = sorted(lst)
    left = 0
    right = len(sorted_lst) - 1
    result = []
    while left <= right:
        # Add the minimum element
        result.append(sorted_lst[left])
        left += 1
        if left > right:
            break
        # Add the maximum element
        result.append(sorted_lst[right])
        right -= 1
    return result