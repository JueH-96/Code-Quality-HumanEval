def find_zero(xs: list):
    a, b = -1.0, 1.0
    fa, fb = poly(xs, a), poly(xs, b)
    if fa == 0:
        return a
    if fb == 0:
        return b
    # expand interval until a sign change bracket is found
    while fa * fb > 0:
        a *= 2
        b *= 2
        fa, fb = poly(xs, a), poly(xs, b)
        if fa == 0:
            return a
        if fb == 0:
            return b
    # bisection method
    for _ in range(100):
        mid = (a + b) / 2
        fm = poly(xs, mid)
        if abs(fm) < 1e-12:
            return mid
        if fa * fm < 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm
    return (a + b) / 2