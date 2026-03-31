def is_sum_of_two(x, y, z):
    def is_integer(n):
        if isinstance(n, bool):
            return False
        try:
            return n == int(n)
        except TypeError:
            return False

    if not (is_integer(x) and is_integer(y) and is_integer(z)):
        return False

    return (x + y == z) or (x + z == y) or (y + z == x)