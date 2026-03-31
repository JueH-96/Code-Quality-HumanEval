def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    if not txt:
        return False
    # If the string ends with a space, the last character isn't valid.
    if txt[-1] == " ":
        return False
    
    last_char = txt[-1]
    # Check if the last character is an alphabetical character.
    if not last_char.isalpha():
        return False
    
    # Determine if the last character is by itself in its word.
    words = txt.split()
    # Get the last word from the string.
    last_word = words[-1] if words else ""
    return len(last_word) == 1