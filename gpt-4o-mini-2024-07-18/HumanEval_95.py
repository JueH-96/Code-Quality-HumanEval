def check_dict_case(dict):
    if not dict:
        return False
    
    keys = dict.keys()
    all_lower = all(isinstance(key, str) and key.islower() for key in keys)
    all_upper = all(isinstance(key, str) and key.isupper() for key in keys)
    
    return all_lower or all_upper