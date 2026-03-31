def compare_one(a, b):
    def parse_value(value):
        if isinstance(value, str):
            value = value.replace(',', '.')
        return float(value) if isinstance(value, (int, float, str)) and value.replace('.', '', 1).isdigit() else value

    a_parsed = parse_value(a)
    b_parsed = parse_value(b)

    if a_parsed == b_parsed:
        return None
    return a if a_parsed > b_parsed else b