def solve(s):
    has_letter = any(c.isalpha() for c in s)
    if has_letter:
        result = []
        for c in s:
            if c.isalpha():
                if c.islower():
                    result.append(c.upper())
                else:
                    result.append(c.lower())
            else:
                result.append(c)
        return ''.join(result)
    else:
        return s[::-1]