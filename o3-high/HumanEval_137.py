def compare_one(a, b):
    """
    Takes two values (int, float, or str representing a real number with '.' or ',' as
    decimal separator) and returns the one with the larger numeric value in its original
    type. Returns None if the numeric values are equal.
    """
    def to_float(x):
        if isinstance(x, str):
            x_clean = x.strip().replace(',', '.')
            return float(x_clean)
        return float(x)
    
    num_a = to_float(a)
    num_b = to_float(b)
    
    # Treat very small differences as equality to avoid floating-point artifacts
    if abs(num_a - num_b) < 1e-12:
        return None
    return a if num_a > num_b else b