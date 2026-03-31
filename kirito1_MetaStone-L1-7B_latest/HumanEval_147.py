import math

def count_zero_mod3_triplets(n):
    if n < 3:
        return 0
    r0_count = ((n - 2) // 3) + 1
    r1_count = n - r0_count
    
    caseA = math.comb(r0_count, 3) if r0_count >= 3 else 0
    caseB = math.comb(r1_count, 3) if r1_count >= 3 else 0
    
    return caseA + caseB