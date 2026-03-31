def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    def parse_value(x):
        if isinstance(x, str):
            x = x.replace(',', '.')
        return float(x)
    
    parsed_a = parse_value(a)
    parsed_b = parse_value(b)
    
    if parsed_a > parsed_b:
        return a
    elif parsed_b > parsed_a:
        return b
    else:
        return None