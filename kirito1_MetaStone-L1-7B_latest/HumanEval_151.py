def double_the_difference(lst):
    total = 0
    for x in lst:
        if type(x) is not int or isinstance(x, bool):
            continue
        if x < 0:
            continue
        if x % 2 != 0:
            total += x ** 2
    return total