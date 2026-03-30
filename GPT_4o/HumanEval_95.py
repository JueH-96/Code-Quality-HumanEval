def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    """
    if not dict:
        return False

    lower_case = all(isinstance(k, str) and k.islower() for k in dict)
    upper_case = all(isinstance(k, str) and k.isupper() for k in dict)

    return lower_case or upper_case