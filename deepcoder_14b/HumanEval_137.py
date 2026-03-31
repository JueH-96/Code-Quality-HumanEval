def compare_one(a, b):
    # Process 'a' to get its numeric value
    if isinstance(a, str):
        a_str = a.replace(',', '.')
        a_num = float(a_str)
    else:
        a_num = float(a)
    
    # Process 'b' to get its numeric value
    if isinstance(b, str):
        b_str = b.replace(',', '.')
        b_num = float(b_str)
    else:
        b_num = float(b)
    
    # Compare the numeric values
    if a_num == b_num:
        return None
    elif a_num > b_num:
        return a
    else:
        return b