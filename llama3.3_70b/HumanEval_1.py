from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')  # Remove all spaces from the string
    result = []  # Initialize an empty list to store the groups of parentheses
    temp = ''  # Initialize a temporary string to build each group of parentheses
    count = 0  # Initialize a counter to keep track of open and close parentheses

    for char in paren_string:  # Iterate over each character in the input string
        if char == '(':  # If an open parenthesis is found, increment the counter
            count += 1
        elif char == ')':  # If a close parenthesis is found, decrement the counter
            count -= 1

        temp += char  # Add the current character to the temporary string

        if count == 0:  # When the counter reaches zero, it means we've found a complete group of parentheses
            result.append(temp)  # Add the group to the result list
            temp = ''  # Reset the temporary string for the next group

    return result