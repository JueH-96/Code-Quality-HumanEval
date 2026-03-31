def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            s = str(abs(num))
            first_digit = s[0]
            last_digit = s[-1]
            if (first_digit in {'1', '3', '5', '7', '9'} and 
                last_digit in {'1', '3', '5', '7', '9'}):
                count += 1
    return count