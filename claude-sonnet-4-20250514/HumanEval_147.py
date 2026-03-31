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
    # Count how many numbers are 0 mod 3 and 1 mod 3
    count_0 = 0  # numbers ≡ 0 (mod 3)
    count_1 = 0  # numbers ≡ 1 (mod 3)
    
    for i in range(1, n + 1):
        val = i * i - i + 1
        if val % 3 == 0:
            count_0 += 1
        else:  # val % 3 == 1
            count_1 += 1
    
    # Calculate combinations
    # C(count_0, 3) for three numbers all ≡ 0 (mod 3)
    # C(count_1, 3) for three numbers all ≡ 1 (mod 3)
    
    def combinations(n, r):
        if n < r or r < 0:
            return 0
        if r == 0 or r == n:
            return 1
        r = min(r, n - r)  # Take advantage of symmetry
        result = 1
        for i in range(r):
            result = result * (n - i) // (i + 1)
        return result
    
    return combinations(count_0, 3) + combinations(count_1, 3)