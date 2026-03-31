def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    uppercase_vowels = {'A', 'E', 'I', 'O', 'U'}
    
    for i in range(0, len(s), 2):  # Check only even indices (0, 2, 4, ...)
        if s[i] in uppercase_vowels:
            count += 1
    
    return count