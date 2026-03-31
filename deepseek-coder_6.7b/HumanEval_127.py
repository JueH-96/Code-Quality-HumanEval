def intersection(interval1, interval2):
    max_start = max(interval1[0], interval2[0])
    min_end = min(interval1[1], interval2[1])
    
    if max_start > min_end:  # No overlap
        return "NO"
        
    intersect_len = min_end - max_start + 1
    
    # Check if the length is a prime number
    for i in range(2, int(intersect_len ** 0.5) + 1):  
        if intersect_len % i == 0:       # Number is not prime
            return "NO"
            
    return "YES"     # Prime length found