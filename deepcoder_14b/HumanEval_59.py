def largest_prime_factor(n):
    if n < 2:
        return -1  # Assuming we return -1 for invalid input or no factors
    
    max_prime = -1

    # Check if n is even
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    # Now check odd numbers from 3 onwards
    i = 3
    while i * i <= n:
        while n % i == 0:
            max_prime = i
            n //= i
        i += 2

    # If remaining n is a prime number greater than 2
    if n > 2:
        max_prime = n

    return max_prime if max_prime != -1 else None

# Example usage:
n = int(input("Enter a number: "))
print(f"The largest prime factor of {n} is {largest_prime_factor(n)}.")