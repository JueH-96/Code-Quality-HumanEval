def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """

    # Normalize string inputs to use '.' as float separator
    if isinstance(a, str):
        a = a.replace(',', '.')
        a_type = str
    else:
        a_type = type(a)
        
    if isinstance(b, str):
        b = b.replace(',', '.')
        b_type = str
    else:
        b_type = type(b)

    # Convert inputs to float for comparison
    a_float = float(a) if not isinstance(a, (int, float)) else a
    b_float = float(b) if not isinstance(b, (int, float)) else b

    # Compare values
    if a_float > b_float:
        return a_type(a) if a_type == str else a
    elif a_float < b_float:
        return b_type(b) if b_type == str else b
    else:
        return None