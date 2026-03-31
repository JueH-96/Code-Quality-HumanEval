def compare_one(a, b):
    a = float(str(a).replace(",", ".")) if isinstance(a, str) else float(a)
    b = float(str(b).replace(",", ".")) if isinstance(b, str) else float(b)

    if a > b:
        return type(a)(a) if not isinstance(a, float) else a
    elif b > a:
        return type(b)(b) if not isinstance(b, float) else b
    else:
        return None