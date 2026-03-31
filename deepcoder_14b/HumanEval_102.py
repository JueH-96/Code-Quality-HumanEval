def choose_num(x, y):
    start = min(x, y)
    end = max(x, y)
    for num in range(end, start - 1, -1):
        if num % 2 == 0:
            return num
    return -1