def correct_bracketing(brackets: str):
    stack = []
    for c in brackets:
        if c == '<':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0