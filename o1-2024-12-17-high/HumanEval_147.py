def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
    For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
    Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

    # Count how many elements are 0 mod 3 and 1 mod 3
    # From the pattern, a[i] mod 3 is 0 if i mod 3 == 2, else 1
    c0 = n // 3 + (1 if n % 3 == 2 else 0)
    c1 = n - c0  # none are 2 mod 3

    def comb3(x):
        return x * (x - 1) * (x - 2) // 6 if x >= 3 else 0

    return comb3(c0) + comb3(c1)