def fib(n: int):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1 or n == 2:
        return 1
    else:
        first = 1
        second = 1
        for _ in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second