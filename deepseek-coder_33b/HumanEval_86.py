def anti_shuffle(s):
    return ''.join(sorted([char for char in word if not char.isspace() else char + "!!!!" for word in s.split()], key=lambda x: (x[0], len(x))))