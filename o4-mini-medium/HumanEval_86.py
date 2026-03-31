def anti_shuffle(s):
    res = []
    word = []
    for c in s:
        if c == ' ':
            if word:
                res.append(''.join(sorted(word)))
                word = []
            res.append(c)
        else:
            word.append(c)
    if word:
        res.append(''.join(sorted(word)))
    return ''.join(res)