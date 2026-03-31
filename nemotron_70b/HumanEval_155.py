def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (0, 3)
    """
    num = abs(num)  # convert to positive for simplicity
    even_count = sum(1 for digit in str(num) if int(digit) % 2 == 0)
    odd_count = len(str(num)) - even_count
    return (even_count, odd_count)