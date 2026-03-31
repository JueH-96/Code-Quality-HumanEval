from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return them as a list.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups: List[str] = []
    current: List[str] = []
    balance = 0

    for ch in paren_string:
        if ch.isspace():
            # ignore any whitespace
            continue
        if ch not in '()':
            # ignore any unexpected characters
            continue

        current.append(ch)

        if ch == '(':
            balance += 1
        else:  # ch == ')'
            balance -= 1

        if balance == 0 and current:
            # Completed a balanced group
            groups.append(''.join(current))
            current = []

    return groups