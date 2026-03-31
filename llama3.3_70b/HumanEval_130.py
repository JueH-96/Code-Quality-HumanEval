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
    def calculate_tri(i, memo):
        if i in memo:
            return memo[i]
        elif i == 0:
            result = 1
        elif i == 1:
            result = 3
        elif i % 2 == 0:
            result = 1 + i / 2
        else:
            # Special handling for the recursive case when n is odd, 
            # to avoid infinite recursion.
            if i - 2 < 0 or i + 1 > n:
                raise ValueError("n is too small")
            result = calculate_tri(i-1, memo) + calculate_tri(i-2, memo) + calculate_tri(i+1, memo)
        memo[i] = result
        return result

    sequence = []
    memo = {}
    for i in range(n + 1):
        sequence.append(calculate_tri(i, memo))
    return sequence