def total_match(lst1, lst2):
    sum_lst1 = sum(len(s) for s in lst1)
    sum_lst2 = sum(len(s) for s in lst2)
    return lst2 if sum_lst1 > sum_lst2 else lst1