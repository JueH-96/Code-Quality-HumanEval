def check_if_last_char_is_a_letter(txt):
    '''
    Returns True if the last character of the string is an alphabetical
    character and stands alone as a single-letter word; otherwise returns False.
    '''
    # Empty string cannot satisfy the condition
    if not txt:
        return False

    # Last character must be an alphabetic letter
    if not txt[-1].isalpha():
        return False

    # Single-letter string qualifies
    if len(txt) == 1:
        return True

    # Letter is a single-word letter only if preceded by a space
    return txt[-2] == ' '