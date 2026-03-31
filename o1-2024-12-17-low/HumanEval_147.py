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
    from math import comb

    count_mod = [0, 0, 0]
    for i in range(1, n + 1):
        val = (i * i - i + 1) % 3
        count_mod[val] += 1

    # Number of valid triples
    return (comb(count_mod[0], 3) +
            comb(count_mod[1], 3) +
            comb(count_mod[2], 3) +
            count_mod[0] * count_mod[1] * count_mod[2])