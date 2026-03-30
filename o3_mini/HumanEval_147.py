def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.
    """
    # Note: For i in 1..n, a[i] = i^2 - i + 1.
    # It turns out that a[i] mod 3 is:
    #   If i % 3 == 1 or 0, then a[i] mod 3 == 1.
    #   If i % 3 == 2, then a[i] mod 3 == 0.
    # Therefore, let:
    #   count1 = number of i's with i % 3 in {0, 1} (which give residue 1)
    #   count0 = number of i's with i % 3 == 2 (which give residue 0)
    #
    # We want count triples (x, y, z) such that (x+y+z) mod 3 == 0.
    # Valid triples can only be (1,1,1) and (0,0,0).
    # Hence, answer = C(count1, 3) + C(count0, 3)
    
    # Count how many numbers i in 1..n are ≡ 2 mod 3, which give residue 0.
    count0 = n // 3 + (1 if n % 3 >= 2 else 0)
    count1 = n - count0  # All other numbers (i %3==1 or 0) yield residue 1
    
    def comb(x):
        if x < 3:
            return 0
        return (x * (x - 1) * (x - 2)) // 6
    
    return comb(count1) + comb(count0)