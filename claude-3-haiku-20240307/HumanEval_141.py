def file_name_check(file_name):
    import re

    # Check if the file name contains more than 3 digits
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'

    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into the substring before and after the dot
    parts = file_name.split('.')
    prefix, suffix = parts[0], parts[1]

    # Check if the prefix starts with a Latin alphabet letter
    if not prefix or not prefix[0].isalpha():
        return 'No'

    # Check if the suffix is one of the valid extensions
    valid_extensions = ['txt', 'exe', 'dll']
    if suffix not in valid_extensions:
        return 'No'

    return 'Yes'