def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    
    last_char = txt[-1]
    if not last_char.isalpha():
        return False
    
    if len(txt) == 1:
        # The only character in the string is a letter, so it's part of no word
        return True 
        
    second_last_char = txt[-2]
    return not second_last_char.isalpha()