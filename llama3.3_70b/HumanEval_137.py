def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    
    # Convert comma to dot for strings
    if isinstance(a, str):
        a = a.replace(',', '.')
    if isinstance(b, str):
        b = b.replace(',', '.')
        
    # Try to convert to float
    try:
        a_float = float(a)
    except ValueError:
        return None  # or raise an error
    
    try:
        b_float = float(b)
    except ValueError:
        return None  # or raise an error

    if a_float > b_float:
        # Return the larger value in its original type
        if isinstance(a, str):
            return a.replace('.', ',')
        else:
            return a
    elif a_float < b_float:
        # Return the larger value in its original type
        if isinstance(b, str):
            return b.replace('.', ',')
        else:
            return b
    else:
        return None