def intersection(interval1, interval2):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        import math
        limit = int(math.sqrt(n))
        for i in range(3, limit + 1, 2):
            if n % i == 0:
                return False
        return True

    s1, e1 = interval1
    s2, e2 = interval2
    start = max(s1, s2)
    end = min(e1, e2)
    if start > end:
        return "NO"
    length = end - start
    return "YES" if is_prime(length) else "NO"