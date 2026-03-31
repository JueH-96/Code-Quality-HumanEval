def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence using dynamic programming.
    
    :param n: The index of the FibFib number to compute (non-negative integer)
    :return: The n-th FibFib number
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize a list to store the first (n+1) FibFib numbers
    fibfibs = [0, 0, 1]
    
    # Compute and store each FibFib number up to the nth
    for i in range(3, n + 1):
        # The next FibFib is the sum of the previous three
        next_fibfib = sum(fibfibs[-3:])
        fibfibs.append(next_fibfib)
    
    # Return the computed nth FibFib number
    return fibfibs[n]