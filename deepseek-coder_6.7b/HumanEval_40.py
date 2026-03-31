def triples_sum_to_zero(l: list):
    n = len(l)
    
    # If the length of list is less than 3 return False
    if n < 3:
        return False
        
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                # If the sum of three elements is zero then returns True
                if l[i] + l[j] + l[k] == 0:
                    return True
    
    # After going through all possible combinations, it's not able to find a triplet that sums up to 0. Hence, return False
    return False