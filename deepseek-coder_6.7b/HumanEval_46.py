def fib4(n: int) -> int:
    if n < 2:  # base cases
        return 0
    elif n == 2:  
        return 2
    else:
        a, b, c = 0, 0, 2  # initial values for n=0, n=1 and n=2
        for _ in range(3, n+1):  # compute the fib number starting from 3 to n
            a, b, c = b, c, a + b + c  
        return c