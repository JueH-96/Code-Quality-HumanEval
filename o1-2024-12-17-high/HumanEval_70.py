def strange_sort_list(lst):
    s = sorted(lst)
    left, right = 0, len(s) - 1
    result = []
    pick_min = True
    while left <= right:
        if pick_min:
            result.append(s[left])
            left += 1
        else:
            result.append(s[right])
            right -= 1
        pick_min = not pick_min
    return result