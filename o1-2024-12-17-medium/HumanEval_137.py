def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    def parse_value(val):
        if isinstance(val, (int, float)):
            return float(val)
        elif isinstance(val, str):
            return float(val.replace(",", "."))
        else:
            raise ValueError("Invalid type")
    
    a_val = parse_value(a)
    b_val = parse_value(b)
    
    if a_val == b_val:
        return None
    elif a_val > b_val:
        return a
    else:
        return b