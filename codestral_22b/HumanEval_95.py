def check_dict_case(d):
    if len(d) == 0:
        return False
    keys = list(d.keys())
    first_key_is_lower = keys[0].islower()
    for key in keys:
        if isinstance(key, str):
            if (first_key_is_lower and not key.islower()) or (not first_key_is_lower and not key.isupper()):
                return False
        else:
            return False
    return True