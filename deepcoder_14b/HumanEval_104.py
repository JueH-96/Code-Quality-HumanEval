def unique_digits(x):
    result = []
    for num in x:
        s = str(abs(num))
        if all(int(c) % 2 != 0 for c in s):
            result.append(num)
    return sorted(result)