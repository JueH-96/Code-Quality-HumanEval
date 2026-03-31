def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    # The element a[i] = i*i - i + 1, when taken modulo 3, yields:
    # - If i % 3 == 0 or i % 3 == 1, then a[i] % 3 == 1.
    # - If i % 3 == 2, then a[i] % 3 == 0.
    #
    # For the sum of three elements to be divisible by 3, the possible residue combinations are:
    # (0, 0, 0) or (1, 1, 1).
    #
    # Count the number of elements with remainder 0 and 1.
    # For i in [1, n]:
    # - Count of i with i % 3 == 2 (i.e., a[i] % 3 == 0):
    count0 = n // 3 + (1 if n % 3 >= 2 else 0)
    # - The remaining indices produce a[i] % 3 == 1:
    count1 = n - count0

    # Function to compute the combinations C(x, 3).
    def choose(x):
        return x * (x - 1) * (x - 2) // 6 if x >= 3 else 0

    return choose(count0) + choose(count1)