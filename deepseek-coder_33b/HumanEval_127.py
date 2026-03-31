def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    intersect = (max(interval1[0], interval2[0]), min(interval1[1], interval2[1]))
    length = intersect[1] - intersect[0] + 1 if intersect[1] >= intersect[0] else 0
    
    return "YES" if is_prime(length) else "NO"