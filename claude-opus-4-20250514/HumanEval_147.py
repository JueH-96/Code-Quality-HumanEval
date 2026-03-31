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
    # Create the array a
    a = []
    for i in range(1, n + 1):
        a.append(i * i - i + 1)
    
    # Count the remainders when divided by 3
    remainder_count = [0, 0, 0]
    for num in a:
        remainder_count[num % 3] += 1
    
    # Count valid triples
    count = 0
    
    # Case 1: All three numbers have remainder 0
    count += remainder_count[0] * (remainder_count[0] - 1) * (remainder_count[0] - 2) // 6
    
    # Case 2: All three numbers have remainder 1
    count += remainder_count[1] * (remainder_count[1] - 1) * (remainder_count[1] - 2) // 6
    
    # Case 3: All three numbers have remainder 2
    count += remainder_count[2] * (remainder_count[2] - 1) * (remainder_count[2] - 2) // 6
    
    # Case 4: One from each remainder (0, 1, 2)
    count += remainder_count[0] * remainder_count[1] * remainder_count[2]
    
    return count