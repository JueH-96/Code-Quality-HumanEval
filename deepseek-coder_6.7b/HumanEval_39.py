def prime_fib(n: int) -> int:
    fib = [0, 1]
    primes = []
    a = 0
    b = 1
    while len(primes) < n+1:
        fib.append(a + b)
        a = b
        b = fib[-1]
        
        if b < 4 and b > 1:  # first two primes are known to be 2,3
            primes += [2, 3]
        elif b % 2 != 0:   # all odd numbers can't be prime except for 1 itself.
            i = 3
            while i * i <= b and b % i != 0:
                if b % i == 0:
                    break
                else:
                    i += 2
            if i * i > b:
                primes += [b]
    return primes[n]