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
    # We'll need up to index n+1 in case n is odd
    trib = [0] * (n + 2)
    # Base cases inferred from examples
    trib[0] = 1
    trib[1] = 3
    
    # Fill in even indices
    for even_idx in range(2, n + 2, 2):
        trib[even_idx] = 1 + even_idx // 2
    
    # Fill in odd indices starting from 3
    for odd_idx in range(3, n + 1, 2):
        trib[odd_idx] = trib[odd_idx - 1] + trib[odd_idx - 2] + trib[odd_idx + 1]
    
    # Return only up to n
    return trib[:n + 1]