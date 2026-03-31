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
    if not string:
        return ''
    
    # Find the longest postfix that is a palindrome
    for i in range(len(string)):
        postfix = string[i:]
        if is_palindrome(postfix):
            # Found the longest palindromic postfix
            # The prefix is everything before this postfix
            prefix = string[:i]
            # Append the reverse of the prefix to make a palindrome
            return string + prefix[::-1]
    
    # This should never be reached since at minimum the last character is a palindrome
    return string