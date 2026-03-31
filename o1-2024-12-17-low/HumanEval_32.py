def find_zero(xs: list):
    import math

    def poly(xs, x):
        return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

    lo, hi = -1e6, 1e6
    f_lo, f_hi = poly(xs, lo), poly(xs, hi)
    if abs(f_lo) < 1e-12:
        return lo
    if abs(f_hi) < 1e-12:
        return hi

    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = poly(xs, mid)
        if abs(f_mid) < 1e-12:
            return mid
        if f_mid * f_lo < 0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid

    return (lo + hi) / 2