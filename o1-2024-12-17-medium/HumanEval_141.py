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
    if file_name.count('.') != 1:
        return 'No'

    name_before_dot, name_after_dot = file_name.split('.')
    
    if not name_before_dot or not name_before_dot[0].isalpha():
        return 'No'
    
    if name_after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    
    digits_count = sum(ch.isdigit() for ch in file_name)
    if digits_count > 3:
        return 'No'
    
    return 'Yes'