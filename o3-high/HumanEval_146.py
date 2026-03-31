def specialFilter(nums):
    """Return the count of numbers in `nums` that are greater than 10
    and whose first and last digits are both odd (1, 3, 5, 7, 9).
    """
    count = 0
    for n in nums:
        if n > 10:
            s = str(n)
            if int(s[0]) % 2 == 1 and int(s[-1]) % 2 == 1:
                count += 1
    return count