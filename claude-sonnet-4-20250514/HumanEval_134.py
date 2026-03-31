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
    
    # Check if last character is alphabetical
    if not txt[-1].isalpha():
        return False
    
    # Check if the last character is not part of a word
    # This means it should be preceded by a space (or be the only character)
    if len(txt) == 1:
        return True
    
    # If there's more than one character, the second-to-last character should be a space
    return txt[-2] == ' '