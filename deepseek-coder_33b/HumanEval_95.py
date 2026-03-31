def check_dict_case(d):
    if not d:
        return False
        
    is_lower = all(k.islower() for k in d if isinstance(k, str))
    is_upper = all(k.isupper() for k in d if isinstance(k, str))
    
    return is_lower or is_upper