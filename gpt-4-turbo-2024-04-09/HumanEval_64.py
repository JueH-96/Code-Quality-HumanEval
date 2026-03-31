def vowels_count(s):
    vowels = 'aeiou'
    count = sum(1 for char in s.lower() if char in vowels)
    if s and s.lower()[-1] == 'y':
        count += 1
    return count