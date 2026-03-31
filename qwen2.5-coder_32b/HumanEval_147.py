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
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count_mod = [0, 0, 0]
    
    for value in a:
        count_mod[value % 3] += 1
    
    # Count the number of valid triples
    total_triples = 0
    
    # Case 1: All three numbers have mod 0
    total_triples += count_mod[0] * (count_mod[0] - 1) * (count_mod[0] - 2) // 6
    
    # Case 2: All three numbers have mod 1
    total_triples += count_mod[1] * (count_mod[1] - 1) * (count_mod[1] - 2) // 6
    
    # Case 3: All three numbers have mod 2
    total_triples += count_mod[2] * (count_mod[2] - 1) * (count_mod[2] - 2) // 6
    
    # Case 4: One number from each mod group
    total_triples += count_mod[0] * count_mod[1] * count_mod[2]
    
    return total_triples