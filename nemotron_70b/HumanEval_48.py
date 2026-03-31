def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    text = ''.join(c for c in text if c.isalnum()).lower()  # remove non-alphanumeric chars and convert to lowercase
    return text == text[::-1]  # compare string with its reverse