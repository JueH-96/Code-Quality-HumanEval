def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the prime Fibonacci number to find.
    
    Returns:
    int: The n-th prime Fibonacci number.
    """
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Initialize the count of prime Fibonacci numbers found so far
    count = 0
    
    # Initialize the current Fibonacci number
    fib_num = 0
    
    while True:
        # Generate the next Fibonacci number
        fib_num = a + b
        
        # Check if the Fibonacci number is prime
        if is_prime(fib_num):
            # Increment the count of prime Fibonacci numbers found so far
            count += 1
            
            # If we've found the n-th prime Fibonacci number, return it
            if count == n:
                return fib_num
        
        # Update the previous two Fibonacci numbers for the next iteration
        a, b = b, fib_num