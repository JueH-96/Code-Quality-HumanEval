def check_dict_case(input_dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    """
    # Return False for empty dictionary
    if not input_dict:
        return False

    # Ensure all keys are strings
    if not all(isinstance(key, str) for key in input_dict):
        return False

    # Check if all keys are lower-case or all are upper-case
    all_lower = all(key.islower() for key in input_dict)
    all_upper = all(key.isupper() for key in input_dict)

    return all_lower or all_upper