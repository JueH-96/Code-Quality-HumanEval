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
    # Determine the maximum index needed.
    # When n is odd, tri(n) depends on tri(n+1). Otherwise, no extra value is needed.
    max_index = n if n % 2 == 0 else n + 1
    
    # Initialize a list to hold tribonacci values from 0 to max_index.
    trib = [0] * (max_index + 1)
    
    for i in range(max_index + 1):
        if i % 2 == 0:  # even index: formula is 1 + n/2
            trib[i] = 1 + i // 2
        else:  # odd index
            if i == 1:
                trib[i] = 3
            else:
                # For odd i > 1, tri(i) = tri(i-1) + tri(i-2) + tri(i+1)
                # Since i+1 is even, we can directly compute it using the formula.
                trib[i] = trib[i - 1] + trib[i - 2] + (1 + (i + 1) // 2)
    
    # Return only the first n+1 elements.
    return trib[:n + 1]