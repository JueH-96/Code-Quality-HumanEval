def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd', False)
    For s = "abcdef", c = "b"  the result should be ('acdef', False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc', True)
    """
    # Convert characters in c to a set for O(1) membership checks
    remove_set = set(c)
    
    # Build the filtered string by excluding characters present in c
    filtered = ''.join(ch for ch in s if ch not in remove_set)
    
    # Check if the filtered string is a palindrome
    is_palindrome = filtered == filtered[::-1]
    
    # Return the tuple as specified
    return (filtered, is_palindrome)