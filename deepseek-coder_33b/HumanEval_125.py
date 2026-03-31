def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for c in txt:
            if ord('a') <= ord(c) <= ord('z'):  # check if the character is a lower-case letter
                order = (ord(c)-ord('a')) % 2 == 1  
                if not order: continue
                count += 1
        return count