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
    counts = [0, 0, 0]
    for i in range(1, n + 1):
        r = (i * i - i + 1) % 3
        counts[r] += 1
    def comb3(x):
        return x * (x - 1) * (x - 2) // 6 if x >= 3 else 0
    return comb3(counts[0]) + comb3(counts[1]) + comb3(counts[2]) + counts[0] * counts[1] * counts[2]