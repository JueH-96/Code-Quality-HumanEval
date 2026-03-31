def even_odd_count(num):
    """Given an integer. return a tuple (count_of_even_digits, count_of_odd_digits).

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    s = str(abs(num))
    evens = sum(c in '02468' for c in s)
    odds = sum(c in '13579' for c in s)
    return (evens, odds)