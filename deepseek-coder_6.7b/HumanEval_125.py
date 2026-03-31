def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for char in txt:
            if char.islower():
                if (ord(char)-97)%2 == 1: # ord('a') is 97, so 'a' corresponds to 0 in the problem statement
                    count += 1
        return count