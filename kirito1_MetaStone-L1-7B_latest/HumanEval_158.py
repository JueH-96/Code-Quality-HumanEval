def find_max(words):
    data = []
    for word in words:
        count = len(set(word))
        data.append((count, word))
    max_count = max(c for c, w in data)
    candidates = [w for c, w in data if c == max_count]
    return min(candidates)