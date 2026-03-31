def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    balance = 0
    for ch in brackets:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
        # If at any point balance is negative, there's a closing bracket
        # without a matching opening bracket.
        if balance < 0:
            return False
    # All opening brackets must be closed.
    return balance == 0