def count_upper(s):
    upper_vowels = 'AEIOU'
    return sum([1 for i in range(len(s)) if s[i] in upper_vowels and i % 2 == 0])