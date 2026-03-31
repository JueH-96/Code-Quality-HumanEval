def any_int(x, y, z):
    if not all(isinstance(i, int) for i in (x, y, z)):
        return False
    else: 
        return abs(y + z - x) <= 1e-9 or abs(x + z - y) <= 1e-9 or abs(x + y - z) <= 1e-9