def iscube(a):
    c = int(round(abs(a)**(1/3)))
    if a < 0:
        c = -c
    return c**3 == a