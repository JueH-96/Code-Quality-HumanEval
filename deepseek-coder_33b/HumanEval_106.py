import math

def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0: # If index is even calculate factorial
            result.append(math.factorial(i))
        else: # If index is odd calculate sum from 1 to index
            result.append(sum(range(1, i + 1)))
    return result