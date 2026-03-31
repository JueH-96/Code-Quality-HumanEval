import re

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with a single dash '-'.
    
    Examples
    --------
    fix_spaces("Example") -> "Example"
    fix_spaces("Example 1") -> "Example_1"
    fix_spaces(" Example 2") -> "_Example_2"
    fix_spaces(" Example   3") -> "_Example-3"
    """
    def replace_spaces(match):
        spaces = match.group(0)
        return '-' if len(spaces) > 2 else '_' * len(spaces)

    # Replace runs of spaces according to the rules
    return re.sub(r' +', replace_spaces, text)