def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        s = str(abs(num))
        total = 0
        for i in range(len(s)):
            d = int(s[i])
            # Determine the sign based on whether the number is negative and it's the first digit of its absolute value
            if num < 0 and i == 0:
                sign = -1
            else:
                sign = +1
            total += d * sign
        if total > 0:
            count += 1
    return count