from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    depth = 0
    buffer = []
    for ch in paren_string:
        if ch == ' ':
            continue
        if ch == '(':
            if depth == 0:
                buffer = []
            buffer.append(ch)
            depth += 1
        elif ch == ')':
            buffer.append(ch)
            depth -= 1
            if depth == 0:
                groups.append(''.join(buffer))
        else:
            # Ignore any other characters
            continue
    return groups