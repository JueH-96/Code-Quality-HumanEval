def solve(s):
    if all(not c.isalpha() for c in s):
        return s[::-1]
    else:
        return ''.join(c.upper() if c.islower() else c.lower() if c.isupper() else c for c in s)