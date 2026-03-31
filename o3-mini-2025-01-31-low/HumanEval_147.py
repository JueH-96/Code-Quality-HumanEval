def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.
    """
    def nC3(x):
        if x < 3:
            return 0
        return x * (x - 1) * (x - 2) // 6

    # Based on analysis, we observe that:
    # For any i, a[i] = i^2 - i + 1. Checking a[i] mod 3:
    # If i % 3 == 1: 1 - 1 + 1 = 1 (mod 3)
    # If i % 3 == 2: 4 - 2 + 1 = 3 ≡ 0 (mod 3)
    # If i % 3 == 0: 0 - 0 + 1 = 1 (mod 3)
    # Hence, a[i] mod 3 is 0 when i % 3 == 2, and 1 otherwise.
    # Let count0 be the count of numbers where a[i] ≡ 0 (i % 3 == 2)
    # and count1 be the count of numbers where a[i] ≡ 1.
    # A triple's sum is divisible by 3 only if:
    #   All three are from count0 (0+0+0=0 mod3) or all three are from count1 (1+1+1=3 mod3).
    
    count0 = (n + 1) // 3  # Numbers i in 1..n with i % 3 == 2
    count1 = n - count0    # The rest have a[i] ≡ 1 mod 3
    
    return nC3(count0) + nC3(count1)