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
    if not string:  # edge case: empty string
        return ''

    for i in range(len(string), -1, -1):  # find longest palindromic postfix
        postfix = string[i:]
        if is_palindrome(postfix):
            prefix = string[:i]  # get prefix before the palindromic suffix
            return string + prefix[::-1]  # append reversed prefix to form palindrome

    # should never reach here, but just in case
    raise AssertionError("Failed to find a palindromic postfix")