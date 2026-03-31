def check_if_last_char_is_a_letter(txt):
    if len(txt.strip()) == 0: return False
    return txt.split()[-1][-1].isalpha() and not txt.split()[-1][:-1].isalpha()