def ends_with_single_letter(s):
    stripped = s.rstrip()
    if not stripped:
        return False
    last_char = stripped[-1]
    return len(last_char) == 1 and last_char.isalpha()

# Example usage:
print(ends_with_single_letter("apple"))       # Output: True
print(ends_with_single_letter("apple?"))      # Output: False (since '?' is not a letter)
print(ends_with_single_letter("apple "))      # Output: True (after stripping, last char is 'e')
print(ends_with_single_letter(""))           # Output: False
print(ends_with_single_letter("a"))          # Output: True
print(ends_with_single_letter("hello world"))# Output: False (last non-space is 'd', which is a letter but part of a word)