def choose_num(x, y):
    if x > y:
        return -1
    elif y % 2 == 0:
        return y
    else:
        return y-1