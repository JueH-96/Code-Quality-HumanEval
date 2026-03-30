from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def max_depth(s: str) -> int:
        max_d = 0
        current_d = 0
        for char in s:
            if char == '(':
                current_d += 1
                if current_d > max_d:
                    max_d = current_d
            elif char == ')':
                current_d -= 1
        return max_d

    return [max_depth(group) for group in paren_string.split()]