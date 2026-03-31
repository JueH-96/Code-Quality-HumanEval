def sort_array(array):
    new_list = list(array)
    if len(new_list) < 2:
        return new_list
    sum_fl = new_list[0] + new_list[-1]
    if sum_fl % 2 == 1:
        return sorted(new_list)
    else:
        return sorted(new_list, reverse=True)