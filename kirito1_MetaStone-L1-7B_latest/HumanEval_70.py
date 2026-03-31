def strange_sort_list(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    result = []
    i = 0
    j = n - 1
    take_min = True
    
    for _ in range(n):
        if take_min:
            result.append(sorted_lst[i])
            i += 1
        else:
            result.append(sorted_lst[j])
            j -= 1
        take_min = not take_min
    
    return result