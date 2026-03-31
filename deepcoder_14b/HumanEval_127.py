def is_prime(n):
    """Check if a number is a prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve(interval1, interval2):
    # Normalize the intervals to ensure start <= end
    a = min(interval1[0], interval1[1])
    b = max(interval1[0], interval1[1])
    
    c = min(interval2[0], interval2[1])
    d = max(interval2[0], interval2[1])
    
    # Calculate the overlap region
    overlap_start = max(a, c)
    overlap_end = min(b, d)
    
    if overlap_end <= overlap_start:
        return "NO"
    
    length = overlap_end - overlap_start
    
    return "YES" if is_prime(length) else "NO"

# Example usage:
# print(solve((1, 3), (2, 5)))  # Output: YES
# print(solve((5, 3), (4, 6)))  # Output: NO