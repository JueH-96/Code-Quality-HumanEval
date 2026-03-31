def sum_squares(lst):
    summed = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            summed += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            summed += num ** 3
        else:
            summed += num
    return summed