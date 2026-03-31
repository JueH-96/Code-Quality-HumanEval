def fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    memo = [0, 0, 1] + [0] * (n - 3)
    
    for i in range(3, n + 1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        
    return memo[-1]