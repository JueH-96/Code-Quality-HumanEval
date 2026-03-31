def reverse_delete(s, c):
    # Create the new string by excluding any character in 'c'
    new_s = ''.join([char for char in s if char not in c])
    # Check if the new string is a palindrome
    is_palindrome = (new_s == new_s[::-1])
    return (new_s, is_palindrome)