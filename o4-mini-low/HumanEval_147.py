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
    # Count of elements with a[i] % 3 == 0 corresponds to i % 3 == 2
    count0 = n // 3 + (1 if n % 3 >= 2 else 0)
    # Remaining elements have a[i] % 3 == 1
    count1 = n - count0

    def comb3(x):
        return x * (x - 1) * (x - 2) // 6 if x >= 3 else 0

    # Triples summing to 0 mod 3: either three 0s or three 1s
    return comb3(count0) + comb3(count1)