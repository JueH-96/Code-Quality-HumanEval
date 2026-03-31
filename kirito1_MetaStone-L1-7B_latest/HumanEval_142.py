def sum_squares(lst):
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            term = num ** 2
        elif i % 4 == 0:
            term = num ** 3
        else:
            term = num
        total += term
    return total