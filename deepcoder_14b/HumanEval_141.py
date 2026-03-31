def is_valid_file_name(file_name):
    # Check if there's exactly one dot in the file name
    if file_name.count('.') != 1:
        return False
    
    try:
        prefix, suffix = file_name.split('.', 1)
    except ValueError:
        return False
    
    # Both parts must be non-empty
    if not prefix or not suffix:
        return False
    
    # The first character of the prefix must be a letter
    if not prefix[0].isalpha():
        return False
    
    # Check if the suffix is one of the allowed extensions (case-insensitive)
    allowed_extensions = {'txt', 'exe', 'dll'}
    if suffix.lower() not in allowed_extensions:
        return False
    
    # Count the number of digits in the entire file name
    digit_count = sum(1 for c in file_name if c.isdigit())
    if digit_count > 3:
        return False
    
    return True