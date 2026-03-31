def count_occurrences(s, substr):
    sub_len = len(substr)
    s_len = len(s)
    
    if sub_len > s_len:
        return 0
    
    count = 0
    for i in range(s_len - sub_len + 1):
        if s[i:i+sub_len] == substr:
            count += 1
            
    return count