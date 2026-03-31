def check_dict_case(d):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    """
    if not d:
        return False
    if not all(isinstance(k, str) for k in d):
        return False
    return all(k.islower() for k in d) or all(k.isupper() for k in d)