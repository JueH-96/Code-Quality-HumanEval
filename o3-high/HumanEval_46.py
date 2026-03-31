def fib4(n: int):
    """Compute the n-th number in the Fib4 sequence (non-recursive).
    
    The Fib4 sequence is defined as:
        fib4(0) -> 0
        fib4(1) -> 0
        fib4(2) -> 2
        fib4(3) -> 0
        fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4
    
    Parameters
    ----------
    n : int
        Index of the element to compute (must be non-negative).
    
    Returns
    -------
    int
        The n-th Fib4 number.
    
    Examples
    --------
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    base = (0, 0, 2, 0)
    if n < 4:
        return base[n]

    a0, a1, a2, a3 = base  # Maintain the last four computed values
    for _ in range(4, n + 1):
        nxt = a0 + a1 + a2 + a3
        a0, a1, a2, a3 = a1, a2, a3, nxt

    return a3