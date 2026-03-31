def poly(xs):
    def evaluate_f(x_val):
        total = 0
        for i, coeff in enumerate(xs):
            if coeff != 0:
                term = coeff * (x_val ** i)
                total += term
        return total

    # Handle different cases based on the length of xs
    if len(xs) == 1:
        c = xs[0]
        if c != 0:
            return None  # No real roots for non-zero constants
        else:
            return 0   # Any x is a root for zero constant

    elif len(xs) == 0:
        # Treat empty list as representing the polynomial f(x)=1 or similar?
        # This is ambiguous, so default to returning None indicating no solution.
        return None

    else:
        def bisection(a, b):
            max_iterations = 50
            tolerance = 1e-7

            for _ in range(max_iterations):
                mid = (a + b) / 2.0
                f_mid = evaluate_f(mid)
                if abs(f_mid) < tolerance:
                    return round(mid, 7)
                # Check sign change
                fafb = evaluate_f(a) * f_mid
                if fafb <= 0:
                    b = mid
                else:
                    a = mid

            return None  # No root found within max iterations

        # Expand search interval to find where the function changes sign
        left = -1e6
        right = 1e6
        fa = evaluate_f(left)
        fb = evaluate_f(right)

        if fa * fb >= 0:
            step = 2.0
            while True:
                new_left = left * 2
                new_right = right * 2

                fn_new_left = evaluate_f(new_left)
                fn_new_right = evaluate_f(new_right)

                # Check for sign change in the expanded interval
                if (fn_new_left * fa) < 0 or (fn_new_right * fb) < 0:
                    left, right = new_left, new_right
                    break

                # If no sign change, expand further to avoid infinite loop
                if abs(new_left - new_right) > max(right + step/2, left - step/2):
                    print("Failed to find interval with opposite signs; increasing search range.")
                    left *= 4.0
                    right *= 4.0
                    fa = evaluate_f(left)
                    fb = evaluate_f(right)
                else:
                    break

            # Perform bisection on the found interval
            root = bisection(left, right)

        return round(root,7) if root is not None else None