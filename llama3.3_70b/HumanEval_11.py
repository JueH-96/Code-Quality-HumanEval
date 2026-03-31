from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Check if input strings have the same length
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length")

    # Initialize an empty list to store XOR results
    xor_results = []

    # Perform binary XOR on each pair of characters in the input strings
    for char_a, char_b in zip(a, b):
        # Check if characters are either '0' or '1'
        if char_a not in ['0', '1'] or char_b not in ['0', '1']:
            raise ValueError("Input strings must consist only of 1s and 0s")
        
        # Perform XOR operation
        xor_result = str(int(char_a) ^ int(char_b))
        xor_results.append(xor_result)

    # Join the XOR results into a single string
    result = ''.join(xor_results)
    
    return result