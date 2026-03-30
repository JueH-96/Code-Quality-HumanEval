def strange_sort_list(lst):
    if not lst:
        return []

    lst.sort()
    result = []
    left, right = 0, len(lst) - 1

    while left <= right:
        result.append(lst[left])
        left += 1
        if left <= right:
            result.append(lst[right])
            right -= 1

    return result