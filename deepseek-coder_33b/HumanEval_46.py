def fib4(n):
    if n < 2: return 0
    elif n == 2: return 2
    sequence = [0, 0, 2] + [0]*(n-3)
    for i in range(3, n+1):
        sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i-3] + sequence[i-4]
    return sequence[n]