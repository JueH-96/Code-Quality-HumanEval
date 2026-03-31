def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    elif txt[-1].isalpha() and (len(txt) == 1 or txt[-2] == ' '):
        return True
    else:
        return False