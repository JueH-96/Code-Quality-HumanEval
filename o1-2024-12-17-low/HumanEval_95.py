def check_dict_case(d):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    """
    if not d:
        return False
    if not all(isinstance(key, str) for key in d):
        return False
    return all(key.islower() for key in d) or all(key.isupper() for key in d)