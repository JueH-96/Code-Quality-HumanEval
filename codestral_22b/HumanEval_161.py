def solve(s):
    result = []
    has_letter = False
    for char in s:
        if char.isalpha():
            has_letter = True
            if char.islower():
                result.append(char.upper())
            else:
                result.append(char.lower())
        else:
            result.append(char)
    if not has_letter:
        result.reverse()
    return ''.join(result)