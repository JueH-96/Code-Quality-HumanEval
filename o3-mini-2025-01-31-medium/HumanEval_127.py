def intersection(interval1, interval2):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    start1, end1 = interval1
    start2, end2 = interval2
    
    inter_start = max(start1, start2)
    inter_end = min(end1, end2)
    
    if inter_end < inter_start:
        return "NO"
    
    # length computed as difference between the bounds
    length = inter_end - inter_start
    if is_prime(length):
        return "YES"
    else:
        return "NO"