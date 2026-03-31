def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n < 0:
        return []
    
    # Initialize a list with the first n+1 terms.
    # Based on the example, we deduce that tri(0) = 1, tri(1) = 3.
    # For even n (n > 0): tri(n) = 1 + (n // 2)
    # For odd n (n > 1): tri(n) = tri(n-1) + tri(n-2) + tri(n+1)
    # Notice: when computing an odd index i, tri(i+1) is even, so it can be computed directly.
    
    seq = [0] * (n + 1)
    # base cases:
    seq[0] = 1
    if n >= 1:
        seq[1] = 3
    
    for i in range(2, n + 1):
        if i % 2 == 0:  # even index
            seq[i] = 1 + (i // 2)
        else:  # odd index
            # compute tri(i+1) using even formula: 1 + ((i+1) // 2)
            next_value = 1 + ((i + 1) // 2)
            seq[i] = seq[i - 1] + seq[i - 2] + next_value
    return seq