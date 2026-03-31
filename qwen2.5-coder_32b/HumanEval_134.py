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
    # Strip any trailing whitespace from the text
    txt = txt.rstrip()
    
    # Check if the string is empty after stripping
    if not txt:
        return False
    
    # Split the text into words
    words = txt.split()
    
    # Get the last word
    last_word = words[-1]
    
    # Check if the last character of the last word is a letter and if it's a single character
    return len(last_word) == 1 and last_word.isalpha()