def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    n = len(string)
    for i in range(n + 1):
        # Check if the substring from index i to end is a palindrome
        if string[i:] == string[i:][::-1]:
            # Append reverse of the substring before the palindromic suffix
            return string + string[:i][::-1]
    return string  # Fallback (shouldn't happen)