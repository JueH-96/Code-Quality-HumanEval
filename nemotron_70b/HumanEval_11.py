from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length")

    for char in a + b:
        if char not in ['0', '1']:
            raise ValueError("Input strings must consist only of 1s and 0s")

    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))