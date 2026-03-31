def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with the supplied string."""
    if not string:
        return ''
    for i in range(len(string)):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            return string + string[:i][::-1]
    return string  # fallback, though logic guarantees earlier return