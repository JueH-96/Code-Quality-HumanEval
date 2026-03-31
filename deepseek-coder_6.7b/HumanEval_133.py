def sum_squares(lst):
    return sum(int(-x) ** 2 if x < 0 else int(x+1) ** 2 for x in lst)