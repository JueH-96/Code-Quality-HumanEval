def calculate_tri(n):
    if n == 0:
        return []
    
    tri_list = [0] * (n + 1)
    tri_list[1] = 3
    
    current_k = 2
    while current_k <= n:
        if current_k % 2 == 0:
            val = (current_k // 2) + 1
            tri_list[current_k] = val
            current_k += 1
        else:
            prev1 = tri_list[current_k - 1]
            prev2 = tri_list[current_k - 2]
            next_term = current_k + 1
            
            if (next_term > n) or (len(tri_list) < next_term):
                raise ValueError("Insufficient computation for this term.")
            
            val_next_even = (next_term // 2) + 1
            tri_list[next_term] = val_next_even
            
            total = prev1 + prev2 + val_next_even
            tri_list[current_k] = total
            
            current_k += 1
    
    return [tri_list[k] for k in range(1, n + 1)]