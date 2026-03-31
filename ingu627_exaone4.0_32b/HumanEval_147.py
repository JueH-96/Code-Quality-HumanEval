def get_max_triples(n):
    count0 = count1 = count2 = 0
    for i in range(1, n+1):
        val = i * i - i + 1
        mod = val % 3
        if mod == 0:
            count0 += 1
        elif mod == 1:
            count1 += 1
        else:
            count2 += 1
    
    total = 0
    # All three are 0 mod 3
    if count0 >= 3:
        total += count0 * (count0 - 1) * (count0 - 2) // 6
    # All three are 1 mod 3
    if count1 >= 3:
        total += count1 * (count1 - 1) * (count1 - 2) // 6
    # All three are 2 mod 3
    if count2 >= 3:
        total += count2 * (count2 - 1) * (count2 - 2) // 6
    # One from each residue
    total += count0 * count1 * count2
    
    return total