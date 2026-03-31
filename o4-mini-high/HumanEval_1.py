def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    s = ''.join(paren_string.split())
    groups = []
    depth = 0
    current = []
    for ch in s:
        if ch == '(':
            if depth == 0:
                current = []
            depth += 1
            current.append(ch)
        elif ch == ')':
            if depth > 0:
                current.append(ch)
                depth -= 1
                if depth == 0:
                    groups.append(''.join(current))
        # ignore other characters
    return groups