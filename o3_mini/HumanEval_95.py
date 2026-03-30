def check_dict_case(dict):
    if not dict:
        return False
    for key in dict:
        if not isinstance(key, str):
            return False
    all_lower = all(key.islower() for key in dict)
    all_upper = all(key.isupper() for key in dict)
    return all_lower or all_upper