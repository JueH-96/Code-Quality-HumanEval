def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'

    before_dot, after_dot = file_name.split('.')

    if not before_dot or not before_dot[0].isalpha() or sum(c.isdigit() for c in before_dot) > 3 or after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'