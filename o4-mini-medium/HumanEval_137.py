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
    def to_num(x):
        if isinstance(x, str):
            try:
                return float(x.replace(',', '.'))
            except ValueError:
                raise ValueError(f"Cannot convert {x!r} to number")
        if isinstance(x, (int, float)):
            return float(x)
        raise TypeError(f"Unsupported type: {type(x)}")

    a_val = to_num(a)
    b_val = to_num(b)

    if a_val > b_val:
        return a
    if b_val > a_val:
        return b
    return None