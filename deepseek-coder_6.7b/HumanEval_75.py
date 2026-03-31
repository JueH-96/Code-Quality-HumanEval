def prime_checker(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 

def is_multiply_prime(a):
    factors = []
    for i in range(2, a+1):
        while a % i == 0 and prime_checker(i):
            if i not in factors:
                factors.append(i)
            a /= i
        if a == 1 or len(factors) > 3: 
            break
    return len(factors) == 3 and a==1