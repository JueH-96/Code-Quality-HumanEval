def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        sum_digits = 0
        temp = abs(num)
        is_negative = num < 0
        digits = []
        if temp == 0:
            digits.append(0)
        else:
            while temp > 0:
                digits.append(temp % 10)
                temp = temp // 10
            digits = digits[::-1]  # Reverse to get the correct order
        if is_negative:
            if digits:
                digits[0] = -digits[0]
        sum_digits = sum(digits)
        if sum_digits > 0:
            count += 1
    return count