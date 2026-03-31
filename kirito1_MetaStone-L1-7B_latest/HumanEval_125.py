def split_words(txt):
    # Check for whitespace presence
    if ' ' in txt:
        return txt.split()
    else:
        # Check for comma presence
        if ',' in txt:
            return txt.split(',')
        else:
            count = 0
            for c in txt:
                lc = c.lower()
                if lc.isalpha():
                    ord_val = ord(lc)
                    if ord_val % 2 == 1:
                        count += 1
            return count