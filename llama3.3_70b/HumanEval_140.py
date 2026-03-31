def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    import re
    # Find all occurrences of one or more spaces
    spaces = re.findall(r' +', text)
    
    if any(len(space) > 2 for space in spaces):
        # Replace all consecutive spaces with -
        return text.replace(' ', '-')
    else:
        # Replace all consecutive spaces with _
        return text.replace(' ', '_')