def circular_shift(x, shift):
    str_x = str(x)
    n = len(str_x)
    if n == 0:
        return ''
    if shift > n:
        reversed_str = ''.join(reversed(str_x))
        return reversed_str
    else:
        rotated_str = str_x[-shift:] + str_x[:-shift]
        return rotated_str