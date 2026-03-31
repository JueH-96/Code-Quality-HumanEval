def change_base(x: int, base: int):
    if x == 0:
        return '0'
    digits = []
    is_negative = False
    if x < 0:
        is_negative = True
        x = abs(x)
    while x > 0:
        rem = x % base
        digits.append(str(rem))
        x = x // base
    result = ''.join(reversed(digits))
    return '-' + result if is_negative else result