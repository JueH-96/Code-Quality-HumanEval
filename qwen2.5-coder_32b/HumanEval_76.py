def is_simple_power(x, n):
    if x == 1:
        return True
    power = 1
    while power < x:
        power *= n
    return power == x