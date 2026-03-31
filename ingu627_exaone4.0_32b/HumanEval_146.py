def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))
            if len(num_str) == 0:
                continue
            first_digit = num_str[0]
            last_digit = num_str[-1]
            if first_digit in '13579' and last_digit in '13579':
                count += 1
    return count