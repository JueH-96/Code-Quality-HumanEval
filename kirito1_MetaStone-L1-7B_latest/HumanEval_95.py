def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case. The function should return False if the given dictionary is empty.
    """
    # Check if the dictionary is empty
    if not dict:
        return False
    
    # Check each key to ensure it's a string
    for k in dict:
        if not isinstance(k, str):
            return False
    
    # Determine if all keys are lowercase or uppercase
    is_all_lower = all(k.islower() for k in dict)
    is_all_upper = all(k.isupper() for k in dict)
    
    return is_all_lower or is_all_upper