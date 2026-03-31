def iscube(a):
    if a == 0:
        return True
    sign = 1 if a > 0 else -1
    v = abs(a)
    c = round(v ** (1/3))
    return sign * (c ** 3) == a