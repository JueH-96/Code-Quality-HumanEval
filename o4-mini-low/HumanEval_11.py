from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")
    result_bits: List[str] = []
    for bit_a, bit_b in zip(a, b):
        if bit_a not in ('0', '1') or bit_b not in ('0', '1'):
            raise ValueError("Input strings must consist only of '0' and '1'")
        # XOR: if bits differ, result is '1'; otherwise '0'
        result_bits.append('1' if bit_a != bit_b else '0')
    return ''.join(result_bits)