def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers must be between 2 and 9 (inclusive).

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not (2 <= base <= 9):
        raise ValueError("Base must be an integer between 2 and 9.")

    if x == 0:
        return '0'

    sign = '-' if x < 0 else ''
    x = abs(x)

    digits = []
    while x:
        digits.append(str(x % base))
        x //= base

    return sign + ''.join(reversed(digits))