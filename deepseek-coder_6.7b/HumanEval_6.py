from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    max_levels = []
    
    for group in paren_string.split(' '):
        stack = [] # Stack to keep track of open parentheses
        level = 0   # Variable to hold the maximum number of nested levels
        
        for chr in group:
            if chr == "(":
                stack.append(chr)  # push onto the stack if it's an opening bracket
            elif chr == ")":
                if len(stack) > 0:  
                    stack.pop()      # pop from the stack if it's a closing bracket and there is at least one open parenthesis
                else:               # If no open parenthesis to pop, it means that this group has incorrect formatting. 
                    level = -1       # Set maximum depth of nesting to -1 (meaning an error) and break the loop
                    break
            if len(stack) > level:  
                level = len(stack)    # Update level with stack's length, indicating new deepest level.
        max_levels.append(level)     # After finishing a group, append its maximum depth of nesting to the list
        
    return max_levels