from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize the empty string for storing the xor results
    res = ""
 
    # Loop through each character in the strings
    for i in range(len(a)):
        if a[i] == b[i]:   # If characters at same position are equal, append '0' to result string
            res += "0"
        else:              # Otherwise, append '1' to result string
            res += "1"
 
    return res