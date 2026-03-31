import math

def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of (i+1) if (i+1) is even
    or the sum of numbers from 1 to (i+1) otherwise.
    """
    result = []
    for k in range(n):
        i = k + 1
        if i % 2 == 0:
            result.append(math.factorial(i))
        else:
            total = (i * (i + 1)) // 2
            result.append(total)
    return result