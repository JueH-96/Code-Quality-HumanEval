def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.
    
    Note:
    a[i] = i^2 - i + 1.
    Observing the residues modulo 3:
      - If i % 3 == 0: a[i] = 9 - 3 + 1 = 7 ≡ 1 (mod 3)
      - If i % 3 == 1: a[i] = 1 - 1 + 1 = 1 ≡ 1 (mod 3)
      - If i % 3 == 2: a[i] = 4 - 2 + 1 = 3 ≡ 0 (mod 3)
    Thus, the array a only contains numbers that are ≡ 1 or ≡ 0 (mod 3).
    
    To have a triple (a[i], a[j], a[k]) whose sum is divisible by 3,
    we must either pick three numbers that are all ≡ 1 (since 1+1+1 = 3)
    or pick three numbers that are all ≡ 0 (since 0+0+0 = 0).
    
    Count the numbers:
      Let count0 be the count of indices i (1 ≤ i ≤ n) with a[i] ≡ 0 (mod 3).
      a[i] ≡ 0 happens when i ≡ 2 (mod 3).
      The number of i from 1 to n with i % 3 == 2 is n // 3,
      plus one extra if n % 3 >= 2.
      
      Let count1 be the rest (i.e. indices with a[i] ≡ 1).
      So count1 = n - count0.
    
    The answer is the number of ways to choose 3 out of count0 plus the
    number of ways to choose 3 out of count1.
    """
    def nC3(x):
        return (x * (x - 1) * (x - 2)) // 6 if x >= 3 else 0

    count0 = n // 3 + (1 if n % 3 >= 2 else 0)
    count1 = n - count0
    return nC3(count0) + nC3(count1)