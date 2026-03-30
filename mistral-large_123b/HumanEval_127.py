def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    start_intersect = max(start1, start2)
    end_intersect = min(end1, end2)

    if start_intersect > end_intersect:
        return "NO"

    length_intersect = end_intersect - start_intersect + 1

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return "YES" if is_prime(length_intersect) else "NO"