def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y