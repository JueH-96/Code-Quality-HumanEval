def has_nesting(s):
    depth = 0
    for char in s:
        if char == '[':
            depth += 1
            if depth >= 2:
                return True
        elif char == ']':
            if depth > 0:
                depth -= 1
    return False