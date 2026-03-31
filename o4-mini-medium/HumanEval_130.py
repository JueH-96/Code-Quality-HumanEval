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
    # Determine how far we need to compute to handle odd dependencies
    max_index = n if n % 2 == 0 else n + 1
    # Ensure at least space for tri(1) and tri(2)
    if max_index < 2:
        max_index = 2
    # Initialize storage
    seq = [0] * (max_index + 1)
    seq[0] = 1
    seq[1] = 3
    # Compute even indices
    for i in range(2, max_index + 1):
        if i % 2 == 0:
            seq[i] = 1 + i // 2
    # Compute odd indices
    for i in range(3, max_index + 1, 2):
        seq[i] = seq[i - 1] + seq[i - 2] + seq[i + 1]
    # Return only up to n
    return seq[:n + 1]