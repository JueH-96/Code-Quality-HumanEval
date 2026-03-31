def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            s = str(num)
            # s is like "-123", so first digit should be negative.
            digit_sum = -int(s[1])
            for ch in s[2:]:
                digit_sum += int(ch)
        else:
            digit_sum = sum(int(ch) for ch in str(num))
        if digit_sum > 0:
            count += 1
    return count