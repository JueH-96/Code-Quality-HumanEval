def sum_squares(lst):
    return sum([int((i ** 0.5) + 1 if i < 0 else (i // 1)) ** 2 for i in lst])