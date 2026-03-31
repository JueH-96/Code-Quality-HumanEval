def get_odd_collatz(n):
    if n <= 0:
        return []
    
    seen = set()
    current = n
    odds = []
    
    while True:
        if current in seen:
            break
        
        seen.add(current)
        
        if current % 2 != 0:
            odds.append(current)
        
        # Compute next term based on evenness of current
        if current % 2 == 0:
            next_term = current // 2
        else:
            next_term = 3 * current + 1
        
        current = next_term
    
    return sorted(list(set(odds)))