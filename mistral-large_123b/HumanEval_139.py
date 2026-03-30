def special_factorial(n):
    def factorial(k):
        if k == 0 or k == 1:
            return 1
        else:
            return k * factorial(k - 1)

    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)

    return result