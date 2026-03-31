def solve(s):
    if any(c.isalpha() for c in s):
        return ''.join(c.upper() if c.islower() else c.lower() for c in s)
    else:
        return s[::-1]