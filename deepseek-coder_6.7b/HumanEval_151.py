def double_the_difference(lst):
    sum = 0
    for i in lst:
        if type(i) == int and i > 0 and i % 2 != 0:
            sum += i**2
    return sum * 2