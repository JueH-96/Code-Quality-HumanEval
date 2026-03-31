def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    """
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    # Split into name and extension
    prefix, ext = file_name.split('.', 1)
    # Prefix should not be empty and should start with an ASCII letter
    if not prefix or not (('a' <= prefix[0] <= 'z') or ('A' <= prefix[0] <= 'Z')):
        return 'No'
    # Extension must be one of the allowed ones
    if ext not in ('txt', 'exe', 'dll'):
        return 'No'
    # Count digits in the entire name
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    return 'Yes'