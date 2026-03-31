def file_name_check(file_name):
    # Check if there is exactly one dot
    if file_name.count('.') != 1:
        return "No"
    
    # Split into parts at the first occurrence of the dot
    try:
        part_before, part_after = file_name.split('.', 1)
    except ValueError:
        # This case shouldn't occur since we checked for exactly one dot earlier
        return "No"
    
    # Check part_before conditions
    if len(part_before) == 0 or not part_before[0].isalpha():
        return "No"
    
    # Check part_after condition
    allowed_extensions = ['txt', 'exe', 'dll']
    if part_after.lower() not in allowed_extensions:
        return "No"
    
    # Count total digits in the entire file name
    digit_count = sum(1 for c in file_name if c.isdigit())
    if digit_count > 3:
        return "No"
    
    # All conditions are satisfied
    return "Yes"