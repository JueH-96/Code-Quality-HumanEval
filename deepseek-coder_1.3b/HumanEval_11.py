from typing import List
def string_xor(a: str, b: str) -> str :  
    """ Input are two strings `a` and `b` consisting only 0s and ones.
        Perform binary XOR on these inputs (ignoring the order), return result also as a list of int digits representing each bit from low to high in string representation, then convert it back into its original form by taking one's complement."""  
     xor_result = "".join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])  # perform XOR operation on characters of strings a and b, result is list (0 or 1) each character from low to high
     ones_comp = ~int(xor_result ,2 ) & 0xff   ;    # take one's complement by subtracting it form binary representation. then convert back into its original numeric value with '&', which ensures the output is always positive or zero because Python int values are signed
     return format(ones_comp,'b').zfill(len(a))      # zeros padding for same length of input string a and result should be binary representation.  This will also work if len(xorResult) != n (where `n` is the number of bits in x), then we return '0's padded