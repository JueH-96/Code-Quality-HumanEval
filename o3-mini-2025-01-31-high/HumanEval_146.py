def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            s = str(num)
            # If the number somehow were negative, remove the '-' sign,
            # but since we require num > 10, s should not start with '-'
            first_digit = int(s[0])
            last_digit = int(s[-1])
            if first_digit % 2 == 1 and last_digit % 2 == 1:
                count += 1
    return count