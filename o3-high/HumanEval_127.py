def intersection(interval1, interval2):
    """Determine whether the length of the intersection of two closed integer
    intervals is a prime number. Return "YES" if it is prime, otherwise "NO".
    If the intervals do not intersect, return "NO".
    """
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        if n % 3 == 0:
            return n == 3
        i = 5
        step = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += step
            step = 6 - step  # alternate between adding 2 and 4 (checks 6k±1)
        return True

    a_start, a_end = interval1
    b_start, b_end = interval2

    inter_start = max(a_start, b_start)
    inter_end = min(a_end, b_end)

    if inter_start >= inter_end:  # no overlap or single-point overlap
        return "NO"

    length = inter_end - inter_start
    return "YES" if is_prime(length) else "NO"