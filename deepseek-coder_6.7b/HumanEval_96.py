def count_up_to(n):
    if n < 2:  # no primes less than 2
        return []
    
    primes = []  
    for possible_prime in range(2, n):
        i = 2
        while i * i <= possible_prime:
            if possible_prime % i == 0:
                break
            i += 1
        else:  # no factors found, so this is a prime
            primes.append(possible_prime)
    return primes