def compare_one(a, b):
    if isinstance(a, str):
        a = float(a.replace(",", "."))
    elif isinstance(b, str):
        b = float(b.replace(",", "."))
        
    if isinstance(a, float) or isinstance(b, float):
        try:
            return max([a, b], key=lambda x: None if not isinstance(x, float) else x)
        except ValueError:  # Both a and b are strings.
            return None
    elif isinstance(a, int) or isinstance(b, int):
        try:
            return max([a, b], key=lambda x: None if not isinstance(x, int) else x)
        except ValueError:  # Both a and b are strings.
            return None