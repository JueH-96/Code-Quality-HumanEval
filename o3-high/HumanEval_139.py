def special_factorial(n):
    """Return the 'Brazilian factorial' (product of all factorials up to n).

    brazilian_factorial(n) = n! * (n-1)! * ... * 1!,  for n >= 1.

    Example
    -------
    >>> special_factorial(4)
    288
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 1:
        raise ValueError("Input must be a positive integer (n >= 1).")

    result = 1          # Will hold the running product of factorials
    current_fact = 1    # Will hold the current factorial value (k!)

    for k in range(1, n + 1):
        current_fact *= k   # compute k!
        result *= current_fact

    return result