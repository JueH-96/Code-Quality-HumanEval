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
    # Function to check if a string is a palindrome
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    # If the input string is already a palindrome, no change is needed
    if is_palindrome(string):
        return string

    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            # Find the suffix that needs to be appended to make the input string a palindrome
            suffix = string[i:][::-1]
            return string + suffix