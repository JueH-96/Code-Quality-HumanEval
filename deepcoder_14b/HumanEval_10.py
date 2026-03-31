def make_palindrome(s):
    if s == s[::-1]:
        return s
    else:
        return s + s[:-1][::-1]