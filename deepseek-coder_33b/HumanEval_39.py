def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def prime_fib(n: int):
    fib = [0, 1]
    primes = []
    
    while len(primes) < n:
        newFib = fib[-1] + fib[-2]
        fib.append(newFib)
        
        if is_prime(newFib):
            primes.append(newFib)
            
    return primes[-1]