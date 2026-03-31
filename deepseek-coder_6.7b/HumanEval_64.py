def vowels_count(s):
    return sum(1 for char in s.lower() if char in 'aeiou') + (s[-1].lower() == 'y')