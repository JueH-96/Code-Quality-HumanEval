def make_palindrome(s):
    n = len(s)
    for l in range(n, 0, -1):
        substr = s[-l:]
        if substr == substr[::-1]:
            break
    x = s[:-l][::-1] if (n - l) > 0 else ''
    return s + x