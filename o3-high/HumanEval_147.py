def get_max_triples(n):
    """
    Given a positive integer n, build an array a of length n where
    a[i] = i*i - i + 1 (1-indexed) and count triples (i<j<k) such that
    a[i] + a[j] + a[k] is divisible by 3.
    """
    # Count indices with (i mod 3) == 2 → a[i] ≡ 0 (mod 3)
    # Count indices with (i mod 3) in {0,1} → a[i] ≡ 1 (mod 3)
    q, r = divmod(n, 3)
    c0 = q + (1 if r == 2 else 0)           # count of elements ≡ 0 (mod 3)
    c1 = 2 * q + (1 if r >= 1 else 0)       # count of elements ≡ 1 (mod 3)

    def comb3(x):
        return x * (x - 1) * (x - 2) // 6 if x >= 3 else 0

    return comb3(c0) + comb3(c1)