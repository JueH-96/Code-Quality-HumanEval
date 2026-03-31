def is_simple_power(x, n):
    if x == 1:
        return True
    while x > 1:
        if x % n != 0:
            return False
        x = x / n
    return True

# Test cases
print(is_simple_power(1, 4)) #=> true
print(is_simple_power(2, 2)) #=> true
print(is_simple_power(8, 2)) #=> true
print(is_simple_power(3, 2)) #=> false
print(is_simple_power(3, 1)) #=> False
print(is_simple_power(5, 3)) #=> false