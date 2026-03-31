def largest_prime_factor(n):
    if n <= 1:
        return None  # Assuming n should be greater than 1 based on problem constraints
    
    # Initialize largest_prime to the smallest possible even prime
    largest_prime = 0
    
    # Handle all factors of 2 first (even numbers)
    while n % 2 == 0:
        largest_prime = max(largest_prime, 2)
        n = n // 2
    
    # Now check for odd factors starting from 3
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest_prime = max(largest_prime, i)
            n = n // i
        i += 2
    
    # If remaining n is a prime number greater than 2
    if n > 1:
        largest_prime = max(largest_prime, n)
    
    return largest_prime