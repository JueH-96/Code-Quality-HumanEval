def choose_num(x, y):
    if x > y:
        return -1
    # Iterate from y down to x inclusive
    for n in range(y, x - 1, -1):
        if n % 2 == 0:
            return n
    return -1  # This line is theoretically unreachable as the loop covers all cases where x <= y and numbers exist between them.