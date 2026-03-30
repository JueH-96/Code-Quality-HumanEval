def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        count = sum((ord(char) - ord('a')) % 2 == 1 for char in txt if 'a' <= char <= 'z')
        return count