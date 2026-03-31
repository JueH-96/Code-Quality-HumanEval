def double_the_difference(lst):
    total = 0
    for number in lst:
        if type(number) == int and number >= 0:
            if number % 2 != 0:
                total += number ** 2
    return total