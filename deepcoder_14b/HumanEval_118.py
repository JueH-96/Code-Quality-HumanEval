def find_vowel(word):
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    max_index = -1
    result = ''
    for i in range(1, len(word) - 1):
        current_char = word[i]
        if current_char in vowels:
            left = word[i-1]
            right = word[i+1]
            if left not in vowels and right not in vowels:
                if i > max_index:
                    max_index = i
                    result = current_char
    return result if max_index != -1 else ''

# Example usage:
print(find_vowel("hello"))  # Output: 'e'
print(find_vowel("xaxebx"))  # Output: 'e'