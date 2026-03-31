def factorial(n):  # Helper Function to calculate Factorial
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

def special_factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= factorial(i)
    return result