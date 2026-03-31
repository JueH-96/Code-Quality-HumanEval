def is_end_character(s):
    trimmed_s = s.strip()
    if not trimmed_s:
        return False
    # Check if last character is an alphabetic letter
    return trimmed_s[-1].isalpha()