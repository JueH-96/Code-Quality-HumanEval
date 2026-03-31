def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    count_even = 0
    count_odd = 0

    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1

    return (count_even, count_odd)