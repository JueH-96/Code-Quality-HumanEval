def find_next_smallest(lst):
    if len(lst) < 2:
        return None
    sorted_lst = sorted(lst)
    min_val = sorted_lst[0]
    for i in range(1, len(sorted_lst)):
        if sorted_lst[i] > min_val:
            return sorted_lst[i]
    return None