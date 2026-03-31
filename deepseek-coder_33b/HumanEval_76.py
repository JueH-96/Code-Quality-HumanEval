def is_simple_power(x, n):
    if x == 1 or n == 1:
        return True
    elif x < n or n <= 0 or (x != n and x % n != 0):
        return False
    
    while x > 1:
        if x % n == 0:
            x /= n
        else:
            break
            
    return x == 1