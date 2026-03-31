def fix_spaces(text):
    result = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] != ' ':
            result.append(text[i])
            i += 1
        else:
            j = i
            while j < n and text[j] == ' ':
                j += 1
            count = j - i
            if count > 2:
                result.append('-')
            else:
                result.append('_' * count)
            i = j
    return ''.join(result)