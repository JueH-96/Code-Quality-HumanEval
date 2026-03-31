def prime_factors(n):
    # Handle the case for n less than 2
    if n < 2:
        return []
    
    factors = []
    
    # Divide out all factors of 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd factors starting from 3
    i = 3
    max_factor = (n ** 0.5) + 1  # Adding 1 to ensure we cover sqrt(n)
    
    while i <= max_factor:
        while n % i == 0:
            factors.append(i)
            n = n // i
            max_factor = (n ** 0.5) + 1  # Update max_factor as n decreases
        
        i += 2
    
    # If remaining n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

# Example usage:
number = 60
print(f"Prime factors of {number} are: {prime_factors(number)}")