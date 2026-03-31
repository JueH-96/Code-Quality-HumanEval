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
    # Last character must be an alphabetical character
    if not txt[-1].isalpha():
        return False
    # If there is only one character and it is a letter, it's by itself.
    if len(txt) == 1:
        return True
    # Check if the character before the last is a letter.
    # If it is, then the last letter is part of a word.
    if txt[-2].isalpha():
        return False
    return True