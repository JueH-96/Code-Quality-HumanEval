def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """

    def parse_num(x):
        if isinstance(x, (int, float)):
            return float(x)
        if isinstance(x, str):
            return float(x.replace(",", "."))
        raise ValueError("Unsupported type")

    a_val = parse_num(a)
    b_val = parse_num(b)

    if a_val == b_val:
        return None
    return a if a_val > b_val else b