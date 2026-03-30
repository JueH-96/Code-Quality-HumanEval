def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".
    """
    # Calculate the intersection interval
    start_int = max(interval1[0], interval2[0])
    end_int = min(interval1[1], interval2[1])
    
    # Check if they intersect
    if start_int > end_int:
        return "NO"
    
    # Length of the intersection is defined as end - start.
    length = end_int - start_int
    if length < 2:
        return "NO"
    
    # Function to check if a number is prime
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
    
    return "YES" if is_prime(length) else "NO"