def is_sorted(lst):
    if len(lst) != len(set(lst)):
        count_dict = {}
        for num in lst:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] > 2:
                return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))