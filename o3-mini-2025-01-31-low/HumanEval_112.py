def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    # Create a set of characters to remove for faster lookup
    removals = set(c)
    # Remove characters from s that are in removals
    filtered = ''.join([char for char in s if char not in removals])
    # Check if filtered string is a palindrome by comparing it to its reverse
    is_palindrome = filtered == filtered[::-1]
    return filtered, is_palindrome