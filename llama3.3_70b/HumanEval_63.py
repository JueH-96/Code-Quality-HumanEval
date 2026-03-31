def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize a list to store the FibFib sequence values
    fib_fib_sequence = [0, 0, 1]
    
    # Compute and store the FibFib sequence values up to the nth term
    for i in range(3, n + 1):
        next_term = sum(fib_fib_sequence[-3:])
        fib_fib_sequence.append(next_term)
    
    return fib_fib_sequence[n]

# Alternatively, you can also use a recursive approach with memoization:
def fibfib_recursive(n: int, memo={}):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib_recursive(1)
    0
    >>> fibfib_recursive(5)
    4
    >>> fibfib_recursive(8)
    24
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Check if the term is already computed and stored in the memo dictionary
    if n not in memo:
        memo[n] = fibfib_recursive(n-1, memo) + fibfib_recursive(n-2, memo) + fibfib_recursive(n-3, memo)
    
    return memo[n]