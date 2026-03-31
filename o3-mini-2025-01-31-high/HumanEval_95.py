def check_dict_case(d):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not d:
        return False
    
    # Ensure all keys are strings.
    for key in d:
        if not isinstance(key, str):
            return False

    # Check if all keys are lower-case or all keys are upper-case.
    all_lower = all(key.islower() for key in d)
    all_upper = all(key.isupper() for key in d)
    
    return all_lower or all_upper