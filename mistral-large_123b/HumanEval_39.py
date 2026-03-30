def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_fib(n):
    fib_gen = fibonacci_sequence()
    count = 0
    result = None
    for num in fib_gen:
        if is_prime(num) and num > 1:
            count += 1
            if count == n:
                result = num
                break
    return result