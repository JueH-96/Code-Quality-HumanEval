def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

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
        return string
    n = len(string)
    for i in range(n):
        substring = string[i:]
        if is_palindrome(substring):
            return string + string[:i][::-1]
    return string + string[:-1][::-1]
```

### Explanation
1. **is_palindrome Function**: This helper function checks if a given string is a palindrome by comparing the string with its reverse.
2. **make_palindrome Function**: 
   - **Base Case Handling**: If the input string is empty, return it immediately.
   - **Finding Longest Palindromic Suffix**: The loop iterates over each possible starting index `i` of the string. For each index, it checks the substring from `i` to the end of the string. If this substring is a palindrome, the loop breaks early.
   - **Constructing the Palindrome**: The original string is combined with the reverse of the prefix (the part before the palindromic suffix) to form the shortest palindrome. For example, for the input "cat", the longest palindromic suffix is "t" (starting at index 2). The prefix "ca" is reversed to "ac" and appended, resulting in "catac".
   
This approach efficiently constructs the shortest palindrome by leveraging the existing palindromic parts of the string, minimizing the number of characters added.