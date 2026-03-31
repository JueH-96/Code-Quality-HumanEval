def check_dict_case(d):
    if not d:
        return False
    keys = list(d.keys())
    lower = 0 
    upper = 0
    for key in keys:
        if type(key) != str:
            return False
        elif key == key.lower():
            lower += 1
        elif key == key.upper():
            upper += 1
        else:
            return False
    if (lower == 0 or upper== 0):
        return True
    else:
        return False