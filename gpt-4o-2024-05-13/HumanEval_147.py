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
    count = 0

    # Count the number of elements in a that are congruent to 0, 1, and 2 modulo 3
    mod_count = [0, 0, 0]
    for num in a:
        mod_count[num % 3] += 1

    # Calculate the number of valid triples
    # Case 1: All three numbers are congruent to 0 modulo 3
    count += mod_count[0] * (mod_count[0] - 1) * (mod_count[0] - 2) // 6

    # Case 2: All three numbers are congruent to 1 modulo 3
    count += mod_count[1] * (mod_count[1] - 1) * (mod_count[1] - 2) // 6

    # Case 3: All three numbers are congruent to 2 modulo 3
    count += mod_count[2] * (mod_count[2] - 1) * (mod_count[2] - 2) // 6

    # Case 4: One number from each congruence class
    count += mod_count[0] * mod_count[1] * mod_count[2]

    return count