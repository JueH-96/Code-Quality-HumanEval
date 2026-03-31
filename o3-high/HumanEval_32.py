def find_zero(xs: list):
    """Return one real root of a polynomial with an odd degree (even number of
    coefficients).  Uses a sign-bracketing search followed by bisection."""
    if len(xs) % 2:  # degree must be odd ⇒ number of coefficients even
        raise ValueError("xs must contain an even number of coefficients")

    def f(t):
        return poly(xs, t)

    tol = 1e-12

    # Quick check at x = 0
    v0 = f(0.0)
    if abs(v0) <= tol:
        return 0.0

    # Expand symmetric interval [-k, k] until a sign change (or a root) is found
    k = 1.0
    for _ in range(1000):  # safety cap
        left, right = -k, k
        f_left, f_right = f(left), f(right)

        if abs(f_left) <= tol:
            return left
        if abs(f_right) <= tol:
            return right

        if f_left * f_right < 0:  # sign change ⇒ root lies in [left, right]
            a, b = left, right
            fa, fb = f_left, f_right
            break
        k *= 2.0
    else:
        raise RuntimeError("Failed to bracket a root")

    # Bisection to refine root
    for _ in range(200):  # sufficient for double precision with tol=1e-12
        mid = (a + b) / 2.0
        fm = f(mid)

        if abs(fm) <= tol or (b - a) / 2.0 <= tol:
            return mid

        if fa * fm < 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm

    return (a + b) / 2.0