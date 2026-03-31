def file_name_check(file_name):
    if (file_name.count('.') == 1 and 
        file_name[:-4].isalpha() and 
        len([char for char in file_name if char.isdigit()]) <= 3 and 
        any(file_name.endswith(ext) for ext in ['txt', 'exe', 'dll'])):
        return "Yes"
    else:
        return "No"