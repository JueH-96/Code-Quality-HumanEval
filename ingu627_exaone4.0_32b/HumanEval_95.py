def check_dict_case(dict):
    if not dict:
        return False
    keys = dict.keys()
    has_lower = False
    has_upper = False
    for key in keys:
        if not isinstance(key, str):
            return False
        if key.islower():
            has_lower = True
        elif key.isupper():
            has_upper = True
        else:
            return False
    return has_lower or has_upper