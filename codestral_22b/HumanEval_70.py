def strange_sort_list(lst):
    lst.sort()
    i, j = 0, len(lst) - 1
    result = []
    while i <= j:
        if len(result) % 2 == 0:
            result.append(lst[i])
            i += 1
        else:
            result.append(lst[j])
            j -= 1
    return result