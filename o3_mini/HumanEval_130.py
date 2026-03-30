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
    # Determine the maximum index we need to compute.
    # If n is odd, tri(n) depends on tri(n+1) so we compute one extra element.
    end = n if n % 2 == 0 else n + 1
    seq = [0] * (end + 1)
    
    # Base cases
    seq[0] = 1
    if end >= 1:
        seq[1] = 3
    
    # Fill the sequence from index 2 to end
    for i in range(2, end + 1):
        if i % 2 == 0:
            # Even case: tri(i) = 1 + i/2
            seq[i] = 1 + i // 2
        else:
            # Odd case: tri(i) = tri(i - 1) + tri(i - 2) + tri(i + 1)
            # Since i + 1 is even, we can compute it directly.
            seq[i] = seq[i - 1] + seq[i - 2] + (1 + (i + 1) // 2)
    
    # Return only the first n+1 elements
    return seq[:n + 1]