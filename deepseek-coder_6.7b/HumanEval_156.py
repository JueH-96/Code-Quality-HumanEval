def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000
    """
    
    # Mapping from arabic numbers to roman numerals
    mapping = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), 
               (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'), 
               (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]
    
    result = ""
    for key, value in mapping:
        while number >= key:   # While the remaining number is large enough to include this key...
            number -= key       # Subtract the key from the number
            result += value      # And add its roman numeral equivalent to the result string
    
    return result.lower()  # Return the final result in lowercase (as required by docstring)