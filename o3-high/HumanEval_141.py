def file_name_check(file_name):
    """Validate file name according to specified rules."""
    # Rule: exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    name, ext = file_name.split('.')
    
    # Rule: valid extension
    if ext not in {'txt', 'exe', 'dll'}:
        return 'No'
    
    # Rule: non-empty name that starts with a Latin letter
    if not name or not name[0].isalpha():
        return 'No'
    
    # Rule: allowed characters in name (letters, digits, underscore)
    for ch in name:
        if not (ch.isalnum() or ch == '_'):
            return 'No'
    
    # Rule: no more than three digits in the entire file name
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    return 'Yes'