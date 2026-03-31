from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """Input is a string containing multiple groups of nested parentheses
    separated by whitespace. For each group, return the deepest level
    (maximum nesting depth) of parentheses.

    Examples
    --------
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depths: List[int] = []
    # Split by any whitespace, ignore empty parts (e.g., consecutive spaces)
    for group in paren_string.split():
        current_depth = max_depth = 0
        for ch in group:
            if ch == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif ch == ')':
                current_depth -= 1
        depths.append(max_depth)
    return depths