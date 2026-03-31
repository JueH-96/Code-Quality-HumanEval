import re
def file_name_check(file_name):
    if len(re.findall('\d', file_name)) > 3 or file_name.count('.') != 1:
        return 'No'
    
    name, ext = file_name.split('.')
    
    if not re.match("^[a-zA-Z]", name) or not ext in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'