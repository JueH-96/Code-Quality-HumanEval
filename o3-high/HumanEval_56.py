def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    balance = 0
    for ch in brackets:
        if ch == "<":
            balance += 1
        elif ch == ">":
            balance -= 1
            if balance < 0:  # encountered a closing bracket without a match
                return False
    return balance == 0