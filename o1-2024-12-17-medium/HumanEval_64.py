def vowels_count(s):
    s_lower = s.lower()
    base_count = sum(1 for c in s_lower if c in "aeiou")
    if s_lower.endswith('y'):
        base_count += 1
    return base_count