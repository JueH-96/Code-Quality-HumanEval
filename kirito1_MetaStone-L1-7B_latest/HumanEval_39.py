def nth_fib_prime(n):
    def is_prime(k):
        if k < 2:
            return False
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if k % p == 0:
                return k == p
        d = k - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if a >= k:
                continue
            x = pow(a, d, k)
            if x == 1 or x == k - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, k)
                if x == k - 1:
                    break
            else:
                return False
        return True

    if n < 1:
        return None
    fib_prev_prev = 0  # F(0)
    fib_prev = 1       # F(1)
    count = 0
    while True:
        current_fib = fib_prev_prev + fib_prev
        if is_prime(current_fib):
            count += 1
            if count == n:
                return current_fib
        # Update for next iteration: F(i+1) will be based on previous two
        fib_prev_prev, fib_prev = fib_prev, current_fib