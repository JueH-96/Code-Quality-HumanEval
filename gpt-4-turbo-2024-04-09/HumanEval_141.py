def file_name_check(file_name):
    import re
    
    # Check for exactly one dot and split the name
    if file_name.count('.') != 1:
        return 'No'
    
    name, extension = file_name.split('.')
    
    # Check if the name starts with a letter and has no more than three digits
    if not name or not name[0].isalpha() or len(re.findall(r'\d', name)) > 3:
        return 'No'
    
    # Check if the extension is one of the allowed types
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'