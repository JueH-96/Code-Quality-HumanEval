def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    # Using the arithmetic series formula: sum = n * (n + 1) // 2
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    return n * (n + 1) // 2