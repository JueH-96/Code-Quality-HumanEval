def any_int(x, y, z):
    if not all([isinstance(i, int) for i in [x, y, z]]):
        return False
    elif x == y + z or y == x + z or z == x + y:
        return True
    else:
        return False