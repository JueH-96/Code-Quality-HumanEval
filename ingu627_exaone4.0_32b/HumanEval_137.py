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
    def convert_to_float(x):
        if isinstance(x, str):
            # Replace comma with dot for proper conversion
            x_replaced = x.replace(',', '.')
            try:
                return float(x_replaced)
            except ValueError:
                # In case the string is not a valid number, return as is (though per problem statement, inputs are valid)
                return float(x)  # This might raise an error, but assuming inputs are valid per problem statement
        elif isinstance(x, (int, float)):
            return float(x)
        else:
            raise TypeError("Unsupported type")

    a_float = convert_to_float(a)
    b_float = convert_to_float(b)

    if a_float > b_float:
        return a
    elif b_float > a_float:
        return b
    else:
        return None