def solve(s):  # Complete this function based on your requirement  
    return ''.join([c.upper() if c.isalpha() and s[i].lower() != c else (''+s[i]) for i, c in enumerate(s)], end ='')