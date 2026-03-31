def compare_one(a, b):
    def str_to_num(s):
        s = str(s).replace(',', '.')
        return float(s)
    
    if isinstance(a, (int, float)):
        num_a = a
    else:
        num_a = str_to_num(a)
    
    if isinstance(b, (int, float)):
        num_b = b
    else:
        num_b = str_to_num(b)
    
    if num_a == num_b:
        return None
    elif num_a > num_b:
        return a
    else:
        return b