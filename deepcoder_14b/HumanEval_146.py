def count_odd_digits(numbers):
    count = 0
    for num in numbers:
        if num <= 10:
            continue
        s = str(num)
        last_digit = int(s[-1])
        if last_digit % 2 == 0:
            continue
        first_digit = int(s[0])
        if first_digit % 2 != 0:
            count += 1
    return count

# Example usage:
nums = [33, -2, -3, 45, 21, 109]
print(count_odd_digits(nums))  # Output: 2