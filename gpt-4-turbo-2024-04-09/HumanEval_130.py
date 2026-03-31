def tri(n):
    if n < 0:
        return []
    
    # Base cases
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    
    # Initialize the list with base values
    trib = [1, 3, 2]
    
    # Calculate further values based on the given conditions
    for i in range(3, n + 1):
        if i % 2 == 0:
            trib.append(1 + i // 2)
        else:
            trib.append(trib[i - 1] + trib[i - 2] + trib[i - 3])
    
    return trib