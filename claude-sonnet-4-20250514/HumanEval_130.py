def tri(n):
    if n == 0:
        return [1]
    
    # Initialize the result list
    result = [0] * (n + 1)
    
    # Base cases
    result[0] = 1
    if n >= 1:
        result[1] = 3
    
    # Fill in even positions first (since they don't depend on future values)
    for i in range(2, n + 1, 2):
        result[i] = 1 + i // 2
    
    # Fill in odd positions (which depend on adjacent values)
    for i in range(3, n + 1, 2):
        result[i] = result[i - 1] + result[i - 2] + result[i + 1]
    
    return result